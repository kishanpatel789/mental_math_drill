provider "aws" {
  region  = var.region
  profile = var.aws_profile
}

data "aws_caller_identity" "current" {}

locals {
  aws_account_id = data.aws_caller_identity.current.account_id
}


resource "aws_iam_role" "lambda_execution_role" {
  name = "mental-math-drill-lambda-execution-tf"

  assume_role_policy = <<-POLICY
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }
  POLICY

  inline_policy {
    name   = "write-logs"
    policy = <<-POLICY
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "logs:CreateLogGroup",
                    "Resource": "arn:aws:logs:${var.region}:${local.aws_account_id}:*"
                },
                {
                    "Effect": "Allow",
                    "Action": [
                        "logs:CreateLogStream",
                        "logs:PutLogEvents"
                    ],
                    "Resource": [
                        "arn:aws:logs:${var.region}:${local.aws_account_id}:log-group:/aws/lambda/${var.lambda_function_name}:*" 
                    ]
                }
            ]
        }
    POLICY
  }

  inline_policy {
    name   = "send-ses-email"
    policy = <<-POLICY
        {
          "Version": "2012-10-17",
              "Statement": [
                  {
                      "Effect": "Allow",
                      "Action": [
                          "ses:SendEmail",
                          "ses:SendRawEmail"
                      ],
                      "Resource": "*"
                  }
              ]        
        }
    POLICY
  }
}

data "archive_file" "lambda_files" {
  type        = "zip"
  source_dir  = "${path.root}/../src/"
  output_path = "${path.root}/lambda_deployment.zip"

  excludes = [".env", "__pycache__"]
}

resource "terraform_data" "archive_lambda_layer" {
  provisioner "local-exec" {
    interpreter = ["/bin/bash", "-c"]
    command     = <<-COMMANDS
        mkdir python
        cp -r ../venv/lib python/
        zip -r layer_content.zip python
        rm -r python
      COMMANDS
  }
}


resource "aws_lambda_function" "lambda_function" {
  function_name = var.lambda_function_name
  role          = aws_iam_role.lambda_execution_role.arn
  filename      = data.archive_file.lambda_files.output_path
  handler       = "main.main"
  runtime       = "python3.10"
  layers        = [aws_lambda_layer_version.lambda_layer.arn]

  environment {
    variables = {
      "MMD_SENDER"    = var.email_sender,
      "MMD_RECIPIENT" = var.email_recipient
    }
  }
}

resource "aws_lambda_layer_version" "lambda_layer" {
  layer_name          = var.lambda_layer_name
  filename            = "${path.root}/layer_content.zip"
  compatible_runtimes = ["python3.10"]

  depends_on = [terraform_data.archive_lambda_layer]
}
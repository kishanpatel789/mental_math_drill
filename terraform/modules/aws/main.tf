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
                        "arn:aws:logs:${var.region}:${local.aws_account_id}:log-group:/aws/lambda/mental-math-drill-tf:*" 
                    ]
                }
            ]
        }
    POLICY
  }
  # replace log group name with lambda resource name ref

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
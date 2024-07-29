terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "local" {}
}

module "aws" {
  source = "./modules/aws"

  email_sender    = var.aws_email_sender
  email_recipient = var.aws_email_recipient
}


# resource "aws_lambda_layer_version" "test_layer" {
#   # (resource arguments)
# }



# import {
#   to = aws_lambda_layer_version.test_layer
#   id = "arn:aws:lambda:us-east-1:655268872845:layer:mental_math_drill_layer:1"
# }
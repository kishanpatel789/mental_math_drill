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
  email_cron_schedule = var.aws_email_cron_schedule
  email_cron_schedule_timezone = var.aws_email_cron_schedule_timezone
}

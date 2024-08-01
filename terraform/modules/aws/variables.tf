variable "region" {
  description = "Region for AWS resoures."
  type        = string
  default     = "us-east-1"
}

variable "aws_profile" {
  description = "Profile to be utilized in local AWS CLI configuration"
  type        = string
  default     = "default"
}

variable "lambda_function_name" {
  description = "Name of lambda function; must be unique in AWS account"
  type        = string
  default     = "mental-math-drill-tf"
}

variable "lambda_layer_name" {
  description = "Name of lambda layer; must be unique in AWS account"
  type        = string
  default     = "mental_math_drill_layer_tf"
}

variable "email_sender" {
  description = "Address of email sender; must be verified on SES"
  type        = string
  nullable    = false
}

variable "email_recipient" {
  description = "Address of email recipient; must be verified on SES if in sandbox"
  type        = string
  nullable    = false
}

variable "email_cron_schedule" {
  description = "Cron schedule of when email should be sent"
  type = string
  default = "5 11 ? * 2-7 *"
}

variable "email_cron_schedule_timezone" {
  description = "Time zone associated with cron schedule for when email should be sent"
  type = string
  default = "UTC"
}
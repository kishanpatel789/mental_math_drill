variable "region" {
  description = "Region for AWS resoures."
  default     = "us-east-1"
  type        = string
}

variable "aws_profile" {
  description = "Profile to be utilized in local AWS CLI configuration"
  default     = "default"
  type        = string
}

variable "bucket_name" {
  description = "Name of S3 bucket; must be globally unique"
  default     = "data-bucket-0987234-kp"
  type        = string
}

variable "lambda_function_name" {
  description = "Name of lambda function; must be unique in AWS account"
  default     = "mental-math-drill-tf"
  type        = string
}

variable "lambda_layer_name" {
  description = "Name of lambda layer; must be unique in AWS account"
  default     = "mental_math_drill_layer_tf"
  type        = string
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
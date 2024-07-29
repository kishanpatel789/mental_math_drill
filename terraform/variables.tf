variable "aws_email_sender" {
  description = "Address of email sender; must be verified on SES"
  type        = string
  nullable    = false
}

variable "aws_email_recipient" {
  description = "Address of email recipient; must be verified on SES if in sandbox"
  type        = string
  nullable    = false
}
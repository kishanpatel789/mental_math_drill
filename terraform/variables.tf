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

variable "aws_email_cron_schedule" {
  description = "Cron schedule of when email should be sent"
  type = string
  default = "5 11 ? * 2-7 *"
}

variable "aws_email_cron_schedule_timezone" {
  description = "Time zone associated with cron schedule for when email should be sent"
  type = string
  default = "UTC"
}
provider "aws" {
  region  = var.region
  profile = var.aws_profile
}

# s3 bucket for data lake
resource "aws_s3_bucket" "bucket_data_lake" {
  bucket        = var.bucket_name
  force_destroy = true
}

provider "aws" {
  region = "${var.region}"
  profile = "${var.aws_profile}"
}

terraform {
  backend "s3" {
    bucket  = "cfortuner-terraform"
    key     = "pong.io-config/terraform.tfstate"
    region  = "us-west-2"
    profile = "colin-aws"
  }
}

# AWS DynamoDB table

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

resource "aws_dynamodb_table" "config" {
  name           = "PongConfiguration"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "Id"

  attribute {
    name = "Id"
    type = "S"
  }

  attribute {
    name = "Config"
    type = "S"
  }

  attribute {
    name = "UpdatedAt"
  }

  attribute {
    name = "CreatedAt"
  }
}

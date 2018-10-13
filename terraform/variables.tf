variable "region" {
  default = "us-west-2"
}

variable "aws_profile" {
  default = "colin-aws"
}

data "aws_vpc" "pong" {
  filter {
    name   = "tag:Name"
    values = ["pong-vpc"]
  }
}

data "aws_subnet" "public" {
  vpc_id = "${data.aws_vpc.pong.id}"

  filter {
    name   = "tag:Name"
    values = ["public"]
  }
}

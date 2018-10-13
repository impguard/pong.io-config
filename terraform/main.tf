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

# AWS Elasticache - Redis


resource "aws_elasticache_subnet_group" "public" {
  name = "public"
  description = "Contains public subnet groups for use by pong elasticache."
  subnet_ids = ["${data.aws_subnet.public.id}"]
}

resource "aws_elasticache_cluster" "dev" {
  cluster_id           = "dev-pong"
  engine               = "redis"
  node_type            = "cache.t2.micro"
  num_cache_nodes      = 1
  parameter_group_name = "default.redis4.0"
  subnet_group_name    = "${aws_elasticache_subnet_group.public.name}"
}

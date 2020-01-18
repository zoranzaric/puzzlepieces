provider "aws" {
  profile = "default"
  region = "us-east-1"
}

resource "aws_instance" "pz-service-node-1" {
  ami = "ami-2757f631"
  instance_type = "t3a.small"
}

resource "aws_instance" "pz-service-node-2" {
  ami = "ami-2757f631"
  instance_type = "t3a.small"
}

resource "aws_instance" "pz-db-node-1" {
  ami = "ami-2757f631"
  instance_type = "t3a.medium"
}
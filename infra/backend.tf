terraform {
  backend "s3" {
    bucket         = "crypto-platform-tf-state-ayesha"
    key            = "eks/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "crypto-platform-terraform-locks"
    encrypt        = true
  }
}
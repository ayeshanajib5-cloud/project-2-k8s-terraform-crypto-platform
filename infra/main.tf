data "aws_availability_zones" "available" {}

module "vpc" {
  source = "./modules/vpc"

  name = "crypto-platform-vpc"
  cidr = "10.0.0.0/16"

  azs            = slice(data.aws_availability_zones.available.names, 0, 2)
  public_subnets = ["10.0.1.0/24", "10.0.2.0/24"]

  project = "crypto-platform"
}

module "eks" {
  source = "./modules/eks"

  cluster_name       = var.cluster_name
  kubernetes_version = "1.32"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.public_subnets

  project = "crypto-platform"
}
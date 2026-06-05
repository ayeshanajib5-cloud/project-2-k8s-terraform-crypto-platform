module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "6.6.1"

  name = var.name
  cidr = var.cidr

  azs            = var.azs
  public_subnets = var.public_subnets

  map_public_ip_on_launch = true
  enable_nat_gateway      = false

  public_subnet_tags = {
    "kubernetes.io/role/elb" = "1"
  }

  tags = {
    Project = var.project
  }
}
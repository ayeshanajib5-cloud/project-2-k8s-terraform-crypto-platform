data "aws_availability_zones" "available" {}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "6.6.1"

  name = "crypto-platform-vpc"
  cidr = "10.0.0.0/16"

  azs            = slice(data.aws_availability_zones.available.names, 0, 2)
  public_subnets = ["10.0.1.0/24", "10.0.2.0/24"]

  map_public_ip_on_launch = true

  enable_nat_gateway = false

  public_subnet_tags = {
    "kubernetes.io/role/elb" = "1"
  }

  tags = {
    Project = "crypto-platform"
  }
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "21.22.0"

  name               = var.cluster_name
  kubernetes_version = "1.32"

  endpoint_public_access  = true
  endpoint_private_access = false

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.public_subnets

  enable_cluster_creator_admin_permissions = true

#  eks_managed_node_groups = {
#    default = {
#      ami_type       = "AL2023_x86_64_STANDARD"
#      instance_types = ["t3.medium"]
#
#      associate_public_ip_address = true
#
#      min_size     = 1
#      max_size     = 2
#      desired_size = 1
#   }
#  }

  tags = {
    Project = "crypto-platform"
  }
}
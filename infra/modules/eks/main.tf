module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "21.22.0"

  name               = var.cluster_name
  kubernetes_version = var.kubernetes_version

  endpoint_public_access  = true
  endpoint_private_access = false

  vpc_id     = var.vpc_id
  subnet_ids = var.subnet_ids

  enable_cluster_creator_admin_permissions = true

  tags = {
    Project = var.project
  }
}
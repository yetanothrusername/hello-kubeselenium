provider "aws" {
  region = "us-west-2"
}

resource "aws_vpc" "eks_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "eks_subnet" {
  vpc_id                  = aws_vpc.eks_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-west-2a"
}

resource "aws_eks_cluster" "hellowkube_cluster" {
  name     = "hellokube-cluster"
  role_arn = aws_iam_role.example_cluster_role.arn
  vpc_config {
    subnet_ids = [aws_subnet.eks_subnet.id]
  }
}

resource "aws_security_group" "eks_hellokube_sg" {
  name        = "eks-hellokube-sg"
  description = "Security group for example hello kube service"

  vpc_id = aws_vpc.eks_vpc.id

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_eks_cluster_security_group_attachment" "hellokube_sg_attachment" {
  cluster_name    = aws_eks_cluster.hellokube_cluster.name
  security_group_id = aws_security_group.hellokube_cluster_sg.id
}


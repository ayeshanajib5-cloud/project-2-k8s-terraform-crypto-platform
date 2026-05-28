# Production-Grade Kubernetes & Terraform Cloud Platform

A cloud-native DevOps project built to demonstrate real-world Kubernetes, Docker, Terraform, CI/CD, monitoring, and microservices deployment using live crypto market data.

---

# Project Overview

This project is a scalable crypto price tracking platform. Users can request live crypto prices through a FastAPI service. The API sends jobs to a Redis queue, worker containers fetch live data from the CoinGecko API, and processed prices are stored in PostgreSQL.

The platform is containerized with Docker, deployed on Kubernetes, monitored using Prometheus and Grafana, and prepared for cloud deployment using Terraform and AWS EKS.

---

# Tech Stack

- Python
- FastAPI
- Docker
- Docker Compose
- Redis
- PostgreSQL
- Kubernetes
- Nginx Ingress Controller
- Horizontal Pod Autoscaler (HPA)
- Prometheus
- Grafana
- GitHub Actions
- Terraform
- AWS EKS

---

# Architecture

```text
User
 |
 | HTTP Request
 v
FastAPI Service
 |
 | Job Queue
 v
Redis
 |
 | Worker Pods
 v
CoinGecko API
 |
 | Store Data
 v
PostgreSQL
 |
 v
Prometheus + Grafana Monitoring
```

---

# Repository Structure

```text
infra/              Terraform infrastructure files
k8s/                Kubernetes manifests
services/api/       FastAPI backend service
services/worker/    Redis worker service
monitoring/         Monitoring configuration
.github/            GitHub Actions workflows
```

---

# Features

- Live crypto price tracking
- CoinGecko API integration
- Redis-based queue processing
- Worker microservice architecture
- PostgreSQL price storage
- Dockerized services
- Kubernetes deployments and services
- ConfigMaps and Secrets
- Liveness and readiness probes
- Rolling update deployment strategy
- Horizontal Pod Autoscaling
- Nginx Ingress routing
- Prometheus metrics
- Grafana monitoring dashboards
- GitHub Actions CI/CD pipeline

---

# API Endpoints

```text
GET  /health
GET  /price/{coin}
POST /track/{coin}
GET  /metrics
GET  /docs
```

Examples:

```text
GET  /price/bitcoin
POST /track/ethereum
```

---

# Local Docker Setup

Run:

```bash
docker compose up --build
```

Open API Dashboard:

```text
http://localhost:8000/docs
```

---

# Kubernetes Deployment

Apply manifests:

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/redis-deployment.yaml
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/services.yaml
kubectl apply -f k8s/api-deployment.yaml
kubectl apply -f k8s/worker-deployment.yaml
kubectl apply -f k8s/hpa.yaml
kubectl apply -f k8s/ingress.yaml
```

Check pods:

```bash
kubectl get pods -n crypto-platform
```

Port forward API:

```bash
kubectl port-forward svc/crypto-api-service 8000:8000 -n crypto-platform
```

Open:

```text
http://localhost:8000/docs
```

---

# Monitoring

Prometheus and Grafana are installed using Helm.

Install monitoring stack:

```bash
helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring --create-namespace
```

Open Grafana:

```bash
kubectl port-forward svc/monitoring-grafana 3000:80 -n monitoring
```

Grafana URL:

```text
http://localhost:3000
```

---

# CI/CD Pipeline

GitHub Actions workflow runs automatically on every push to the main branch.

The pipeline:
- checks out code
- installs Python dependencies
- builds API Docker image
- builds worker Docker image

---

# Production Practices Implemented

- Microservices architecture
- Containerized workloads
- Kubernetes orchestration
- Health checks
- Readiness checks
- Autoscaling
- ConfigMaps and Secrets
- Ingress routing
- Monitoring and observability
- Git-based workflow
- CI/CD automation

---

# Screenshots

Add screenshots here:

```text
1. FastAPI Swagger dashboard
2. Kubernetes pods
3. Kubernetes services
4. HPA status
5. Grafana dashboard
6. Prometheus dashboard
7. GitHub Actions success
8. Ingress health endpoint
```

---

# Future Improvements

- Deploy to AWS EKS using Terraform
- Add AWS ECR image registry
- Add CloudWatch logging
- Add production IAM least-privilege roles
- Add remote Terraform state using S3 and DynamoDB
- Add HTTPS with cert-manager
- Add authentication for API endpoints

---

# Status

Local production-style Kubernetes deployment is complete.

Cloud deployment with Terraform and AWS EKS is planned as the next phase.
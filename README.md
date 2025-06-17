# 🚀 Flask App on Kubernetes with Helm 

This repository contains a simple Python Flask web application deployed to a Kubernetes cluster using Helm. It supports access via `kubectl port-forward` and optionally through Ingress.

---

## 🧱 Features

- Lightweight Flask web app
- Dockerized for portability
- Deployed via Helm chart
- Supports Kubernetes Service (port-forward) and Ingress
- Customizable via `values.yaml`

---

## 🐳 Docker Setup

### 1. Build the Docker Image
```bash
docker build -t tejaswinelluri/flask-k8s-app:latest .
```

### 2. Push to Docker Hub
```bash
docker push tejaswinelluri/flask-k8s-app
```

Update `image.repository` and `image.tag` in your Helm `values.yaml` file accordingly.

---

## ☸️ Deploy to Kubernetes with Helm

### 1. Install the Chart
```bash
cd helm
helm install flask-release flask-app
```

### 2. Upgrade the Release
```bash
helm upgrade flask-release flask-app
```

### 3. Uninstall the Release
```bash
helm uninstall flask-release
```

---

## 🌐 Accessing the Application

### Port Forwarding
```bash
kubectl port-forward service/flask-app 8080:8080
```

Then access in your browser:
```
http://localhost:8080
```

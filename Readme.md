# CineOps Movie Explorer – DevOps Pipeline Project

## Overview

CineOps Movie Explorer is a web application that allows users to explore trending movies, view details, watch trailers, and search for movies using data from the TMDB API.

This project demonstrates a **complete DevOps workflow**, including containerization, CI/CD automation, infrastructure provisioning, security scanning, and cloud deployment.

The application is built with **Django**, containerized using **Docker**, deployed using **Terraform on AWS EC2**, and automated through a **Jenkins CI/CD pipeline**.

---

## Youtube Demo Link
https://youtu.be/JKkYN8S5ynw

---

## Live Deployment

The CineOps Movie Explorer application is deployed on an AWS EC2 instance and accessible via the public IP.

**Live Application URL**

http://54.242.152.165:8000/

Users can open the above link in a browser to access the deployed application running inside a Docker container on AWS.

**Github Repository link**
https://github.com/yash15808/cineops-devops.git

---

# Project Architecture

```
Developer
   │
   ▼
GitHub Repository
   │
   ▼
Jenkins CI/CD Pipeline
   │
   ▼
Security Scan (Trivy)
   │
   ▼
Terraform Infrastructure
   │
   ▼
AWS EC2 Instance
   │
   ▼
Docker Container
   │
   ▼
Django CineOps Web Application
```

---

# Features

* Browse **Trending Movies**
* **Search movies by title**
* **Watch trailers** from YouTube
* **View movie details**
* **Favorites system**
* **Modern dark UI design**
* Containerized deployment with **Docker**
* Automated infrastructure provisioning with **Terraform**
* **CI/CD pipeline** with Jenkins
* **Security scanning** using Trivy

---

# Tech Stack

## Backend

* Python
* Django

## Frontend

* HTML
* CSS
* JavaScript

## DevOps Tools

* Docker
* Jenkins
* Terraform
* AWS EC2
* Trivy Security Scanner
* GitHub

---

# Project Structure

```
cineops-devops
│
├── cineops/
│   └── Django project settings
│
├── movies/
│   └── Movie app logic
│
├── templates/
│   └── HTML templates
│
├── terraform/
│   └── main.tf
│
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── manage.py
└── README.md
```

---

# Running the Project Locally

## 1. Clone the Repository

```
git clone https://github.com/yash15808/cineops-devops.git
cd cineops-devops
```

## 2. Install Dependencies

```
pip install -r requirements.txt
```

## 3. Run Django Server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

---

# Running with Docker

## Build Docker Image

```
docker build -t cineops .
```

## Run Container

```
docker run -d -p 8000:8000 cineops
```

Access the app:

```
http://localhost:8000
```

---

# Jenkins CI/CD Pipeline

The Jenkins pipeline automates the build and deployment process.

## Pipeline Stages

### 1. Checkout Code

Fetch latest code from the GitHub repository.

### 2. Security Scan

Terraform configuration is scanned using **Trivy** to detect vulnerabilities.

### 3. Terraform Initialization

Initializes Terraform environment.

### 4. Terraform Plan

Shows infrastructure changes before deployment.

### 5. Terraform Apply

Creates AWS infrastructure.

---

# Terraform Infrastructure

Terraform provisions AWS resources including:

* **EC2 Instance (t2.micro)**
* **Security Group**
* **Public IP for application access**

Example commands:

```
terraform init
terraform apply
```

After deployment, Terraform outputs the **public IP address** of the EC2 instance.

---

# Application Deployment on AWS

Once infrastructure is created:

## 1. Connect to EC2 instance

```
ssh ec2-user@PUBLIC_IP
```

## 2. Install Docker

```
sudo yum install docker git -y
sudo systemctl start docker
```

## 3. Clone Repository

```
git clone https://github.com/yash15808/cineops-devops.git
cd cineops-devops
```

## 4. Build and Run Container

```
sudo docker build -t cineops .
sudo docker run -d -p 8000:8000 cineops
```

Access the deployed application:

```
http://54.242.152.165:8000/
```

---

# Security Vulnerability Demonstration

To demonstrate DevOps security practices, the Terraform configuration initially includes an **intentional vulnerability**.

Example insecure rule:

```
cidr_blocks = ["0.0.0.0/0"]
```

This exposes **SSH access to the entire internet**, which is considered a security risk.

---

# Security Scan

The Jenkins pipeline uses **Trivy** to scan Terraform configuration and detect misconfigurations.

---

# AI-Based Remediation

AI tools such as **GitHub Copilot or ChatGPT** analyze the vulnerability and recommend restricting access.

Example fix:

```
cidr_blocks = ["YOUR_IP/32"]
```

This restricts SSH access to a **trusted IP address**, improving infrastructure security.

---

# Security Best Practices

* Limit SSH access to trusted IPs
* Use containerized deployments
* Scan infrastructure code for vulnerabilities
* Avoid exposing sensitive ports publicly

---

# Screenshots

Include the following screenshots in your submission:

* Jenkins pipeline success
* AWS EC2 instance running
* Terraform apply output
* CineOps application running on AWS

---

# Future Improvements

* Deploy using **Kubernetes**
* Add **automated Docker deployment in CI/CD**
* Add **user authentication**
* Use **AWS RDS instead of SQLite**
* Implement **API caching**

---

# GenAI Usage Report

## AI Tools Used

The following Generative AI tools were used during the development of this project:

* **ChatGPT (OpenAI)** – used for troubleshooting DevOps setup, infrastructure configuration, debugging deployment issues, and generating documentation.
* **GitHub Copilot** – used to assist with UI improvements and Django code generation.

---

## How AI Assisted the Project

AI tools were used to support development and DevOps tasks including:

* Generating UI improvements for the movie browsing interface
* Debugging Docker containerization issues
* Assisting with Jenkins pipeline configuration
* Helping configure Terraform infrastructure for AWS EC2
* Identifying security vulnerabilities in Terraform configuration
* Suggesting remediation strategies for insecure firewall rules

---

## Example AI Contribution

**Problem**

Terraform security group allowed SSH access from anywhere:

```
cidr_blocks = ["0.0.0.0/0"]
```

This configuration exposes the server to potential brute-force attacks.

**AI Recommendation**

Restrict SSH access to a specific trusted IP address:

```
cidr_blocks = ["YOUR_IP/32"]
```

This reduces attack surface and follows infrastructure security best practices.

---

## Impact of AI Assistance

The use of Generative AI helped:

* Accelerate development and debugging
* Improve UI and application usability
* Enhance infrastructure security awareness
* Reduce configuration errors in DevOps tools

AI was used as a **support tool**, while the developer reviewed, validated, and implemented all final configurations.

---

## Project Screenshots

### Jenkins CI/CD Pipeline
![Jenkins Pipeline](screenshots/jenkins-pipeline-success.png)

### AWS EC2 Instance Running
![AWS EC2](screenshots/aws-ec2-instance.png)

### Terraform Infrastructure Deployment
![Terraform Apply](screenshots/terraform-apply.png)

### CineOps Application Running on AWS
![Live App](screenshots/cineops-live-aws.png)

---

# Author

**Yash Yadav**
DevOps Assignment – CineOps Movie Explorer

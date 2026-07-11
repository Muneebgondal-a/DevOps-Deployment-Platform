# 🚀 DevOps Control Center

A modern **DevOps Dashboard** built with **Python Flask**, **Docker**, and **Jenkins CI/CD** to monitor system resources, manage Docker containers, and automate deployment workflows.

---

## 📌 Overview

The DevOps Control Center is designed to provide a centralized dashboard for monitoring server resources and managing application deployments. It combines essential DevOps tools into a simple web interface suitable for learning and demonstration purposes.

---

## ✨ Features

### 🔐 Authentication

* Secure login system
* Protected dashboard routes

### 🖥 System Monitoring

* CPU Usage
* Memory Usage
* Disk Usage
* Hostname
* Server IP Address
* Operating System
* System Uptime
* Running Processes

### 🐳 Docker Management

* View Docker containers
* View Docker images
* Start containers
* Stop containers
* Restart containers
* Remove containers

### 🌿 Git Integration

* Current Git branch
* Latest commit information

### 🚀 Deployment

* Deployment dashboard
* Deployment status

### 📄 Logs

* View application logs

### ❤️ Health Check API

```text
GET /health
```

Returns:

```json
{
    "status": "UP",
    "application": "DevOps Control Center",
    "version": "1.0.0"
}
```

---

## 🛠 Technologies Used

* Python
* Flask
* HTML5
* CSS3
* Docker
* Docker Compose
* Jenkins
* Git
* GitHub

---

## 📂 Project Structure

```text
DevOps-Deployment-Platform/
│
├── Backend/
│   ├── app.py
│   ├── routes.py
│   ├── auth.py
│   ├── config.py
│   ├── templates/
│   ├── static/
│   └── services/
│
├── docker-compose.yml
├── Dockerfile
├── Jenkinsfile
├── README.md
└── requirements.txt
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Muneebgondal-a/DevOps-Deployment-Platform.git
```

Navigate to the project:

```bash
cd DevOps-Deployment-Platform
```

Install dependencies:

```bash
pip install -r Backend/requirements.txt
```

Run the application:

```bash
cd Backend
python app.py
```

Open your browser:

```text
http://localhost:5000
```

---

## 🐳 Run with Docker

```bash
docker compose up --build
```

---

## 🔄 CI/CD

The project uses Jenkins to automate the build process.

Workflow:

* Push code to GitHub
* GitHub Webhook triggers Jenkins
* Jenkins checks out the latest code
* Docker image is built
* Application is deployed

---

## 📸 Screenshots

Add screenshots here after uploading them.

Example:

* Dashboard
* Docker Page
* Server Status
* Jenkins Successful Build

---

## 🎯 Learning Outcomes

This project helped me gain hands-on experience with:

* DevOps fundamentals
* CI/CD pipelines
* Docker containerization
* Git & GitHub workflow
* Jenkins automation
* Flask web development
* System monitoring
* Deployment automation

---

## 👨‍💻 Author

**Muneeb Gondal**

Aspiring DevOps Engineer passionate about automation, cloud technologies, containerization, and CI/CD.

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://linkedin.com/in/YOUR_PROFILE

---

## 📄 License

This project is created for educational and portfolio purposes.

<img width="959" height="481" alt="Screenshot 2026-07-11 074704" src="https://github.com/user-attachments/assets/52ee1141-8266-4be9-9473-3f2aacf42cac" />
<img width="956" height="483" alt="Screenshot 2026-07-11 074650" src="https://github.com/user-attachments/assets/6bce18ea-d3df-4ff8-bd9d-d32c84643619" />
<img width="958" height="483" alt="Screenshot 2026-07-11 074629" src="https://github.com/user-attachments/assets/31e14e24-f3b5-4197-809d-037ab7ebd61d" />
<img width="959" height="482" alt="Screenshot 2026-07-11 074614" src="https://github.com/user-attachments/assets/bcf5f821-cd8d-4f7c-a94e-5b748ff58d08" />
<img width="958" height="484" alt="Screenshot 2026-07-11 074601" src="https://github.com/user-attachments/assets/c5223e4c-8c32-45e1-abb1-06c600ca7df0" />
<img width="958" height="479" alt="Screenshot 2026-07-11 074534" src="https://github.com/user-attachments/assets/42e51619-ab08-4330-b95e-c1f63738678b" />


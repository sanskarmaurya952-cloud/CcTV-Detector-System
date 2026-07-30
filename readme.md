# 🛡️ SentinelAI
### AI-Powered CCTV & IoT Security Monitoring Platform

> **"Monitor. Detect. Protect."**

SentinelAI is an enterprise-grade AI-powered SaaS platform that continuously monitors CCTV cameras and IoT surveillance devices in real time. It detects suspicious activities, abnormal camera behavior, security threats, and device failures while providing intelligent alerts, analytics, and actionable insights through a modern web dashboard.

---

## 👥 Team Information

### 🏆 Team Name

# **ALPHA++**

### 👨‍💼 Team Leader

- **Sanskar Maurya**

### 👨‍💻 Team Members

- Sanskar Maurya *(Team Leader)*
- Rahul Kumar
- Rachit Gupta
- Saksham Sahu

---

# 🚀 Project Overview

Traditional CCTV systems only record videos. They cannot determine whether cameras are functioning correctly or whether suspicious incidents require immediate attention.

**SentinelAI** transforms traditional surveillance into an intelligent AI-powered monitoring platform.

The platform allows users to:

- Create an account
- Securely login
- Add multiple RTSP/IP cameras
- Monitor live camera feeds
- Detect suspicious activities using AI
- Monitor camera health in real time
- Receive intelligent alerts
- Analyze security events through an interactive dashboard

SentinelAI is designed as a **multi-tenant SaaS platform**, allowing multiple organizations and users to securely manage their own surveillance infrastructure from a single cloud-based application.

---

# 🎯 Problem Statement

Modern surveillance systems suffer from several limitations:

- Cameras only record footage
- No proactive threat detection
- Camera failures remain unnoticed
- No automatic health monitoring
- Security teams manually monitor screens
- No intelligent incident analysis
- High operational cost
- Delayed response to critical incidents

---

# 💡 Our Solution

SentinelAI combines Artificial Intelligence, Computer Vision, and Cloud Technologies to create an intelligent surveillance platform capable of:

- Real-Time AI Monitoring
- Suspicious Activity Detection
- Camera Health Monitoring
- Trust Score Calculation
- Live Alerts
- Incident Timeline
- AI-Based Analytics
- Predictive Monitoring

---

# ✨ Features

## 🔐 Authentication

- User Registration
- Secure Login
- JWT Authentication
- Multi-user Support
- Role-Based Access

---

## 📹 Camera Management

- Add Unlimited RTSP Cameras
- Live Camera Preview
- Camera Configuration
- Camera Status Monitoring
- Auto Camera Reconnection

---

## 🤖 AI Surveillance

Current Features

- Person Detection
- Intrusion Detection
- Suspicious Activity Detection

Upcoming Features

- Weapon Detection
- Fire Detection
- Smoke Detection
- Loitering Detection
- Face Recognition
- Fall Detection

---

## ❤️ Camera Health Monitoring

Automatically detects:

- Camera Offline
- Frozen Video
- Black Screen
- Blurred Lens
- Covered Camera
- Low FPS
- Network Failure
- Camera Disconnect

---

## 📊 Trust Score Engine

Every connected camera receives a dynamic **Trust Score** calculated using:

- Camera Availability
- Image Quality
- FPS
- Latency
- Detection Reliability
- Camera Health

---

## 🚨 Intelligent Alert System

- Real-Time Alerts
- Suspicious Activity Alerts
- Camera Failure Alerts
- Dashboard Notifications
- Alert History
- Incident Timeline

---

## 📈 Dashboard

The dashboard provides:

- Live Camera Monitoring
- Camera Status
- Camera Health
- Trust Score
- Alert Statistics
- Recent Events
- AI Insights
- Security Analytics

---

# 🏗️ System Architecture

```text
                    SentinelAI

                React Dashboard

                        │

                        ▼

                 FastAPI Backend

                        │

         ┌──────────────┼───────────────┐

         ▼                              ▼

 Authentication                 Camera Manager

                                        │

                                        ▼

                               Camera Sessions

                                        │

                                        ▼

                                  RTSP Streams

                                        │

                                        ▼

                                 Frame Cache

                                        │

               ┌────────────────────────┼──────────────────────┐

               ▼                        ▼                      ▼

       AI Detection Engine      Camera Health Engine    Alert Engine

               │                        │

               └───────────────┬────────┘

                               ▼

                        Trust Score Engine

                               │

                               ▼

                         PostgreSQL Database

                               │

                               ▼

                       Dashboard & Analytics
```

---

# 🧠 AI Processing Pipeline

```text
RTSP Camera

      │

      ▼

Frame Capture

      │

      ▼

Object Detection (YOLO)

      │

      ▼

Suspicious Activity Detection

      │

      ▼

Camera Health Monitoring

      │

      ▼

Trust Score Engine

      │

      ▼

Alert Generation

      │

      ▼

Dashboard Analytics
```

---

# 🛠️ Technology Stack

## Frontend

- React
- TypeScript
- Tailwind CSS
- Axios

---

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication

---

## AI & Computer Vision

- OpenCV
- YOLO
- NumPy

---

## Infrastructure

- Docker
- Redis *(Upcoming)*
- Celery *(Upcoming)*
- WebSockets *(Upcoming)*

---

# 📂 Project Structure

```text
SentinelAI/

│

├── backend/

│ ├── api/

│ ├── core/

│ ├── db/

│ ├── models/

│ ├── repositories/

│ ├── schemas/

│ ├── services/

│ ├── utils/

│ └── main.py

│

├── frontend/

│

├── docs/

│

├── docker/

│

├── README.md

│

└── docker-compose.yml
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/SentinelAI.git

cd SentinelAI
```

---

## Backend Setup

```bash
cd backend

python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Backend

```bash
uvicorn app.main:app --reload
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# 🌟 Current Development Status

- ✅ Authentication
- ✅ Camera Management
- ✅ RTSP Streaming
- ✅ Live Dashboard
- ✅ Object Detection
- 🚧 Camera Health Engine
- 🚧 Trust Score Engine
- 🚧 Alert Engine
- 🚧 Analytics Dashboard
- 🚧 AI Copilot

---

# 🗺️ Roadmap

## Phase 1

- User Authentication
- Camera Management
- Live Streaming

## Phase 2

- AI Object Detection
- Suspicious Activity Detection
- Camera Health Engine

## Phase 3

- Trust Score Engine
- Real-Time Alerts
- Incident Timeline

## Phase 4

- AI Copilot
- Predictive Camera Maintenance
- Mobile Application

---

# 🔮 Future Scope

- Face Recognition
- License Plate Recognition
- PPE Detection
- Crowd Monitoring
- Vehicle Detection
- Fire & Smoke Detection
- Weapon Detection
- Edge AI Deployment
- Kubernetes Deployment
- Cloud Multi-Tenant SaaS
- AI Incident Report Generator

---

# 🏆 Competitive Advantages

✅ AI-Powered Monitoring

✅ Camera Health Detection

✅ Trust Score Engine

✅ Multi-Camera Support

✅ Enterprise SaaS Architecture

✅ Real-Time Analytics

✅ Intelligent Alerts

✅ Scalable Design

---

# 📈 Potential Applications

- Smart Cities
- Industrial Surveillance
- Campus Security
- Airports
- Railway Stations
- Hospitals
- Banks
- Warehouses
- Retail Stores
- Corporate Offices

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create your feature branch

3. Commit your changes

4. Push your branch

5. Create a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 💙 Built with Passion by Team ALPHA++

## 👨‍💼 Team Leader

**Sanskar Maurya**

---

## 👨‍💻 Team Members

- Sanskar Maurya
- Rahul Kumar
- Rachit Gupta
- Saksham Sahu

---

# 🌍 Vision

Our vision is to build an intelligent surveillance platform that not only detects security threats but also monitors the health, reliability, and trustworthiness of surveillance devices using Artificial Intelligence.

We believe the future of surveillance is proactive, intelligent, and autonomous.

---

# ⭐ Show Your Support

If you like this project,

⭐ Star this repository

🍴 Fork this repository

💬 Share your feedback

🚀 Contribute to SentinelAI

---

# 🚀 SentinelAI

**AI-Powered CCTV & IoT Security Monitoring Platform**

### **Monitor • Detect • Protect**
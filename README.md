# Self-Healing Infrastructure Platform

A modular DevOps project that simulates a lightweight self-healing infrastructure platform capable of monitoring system resources, processes, networks, logs, and Docker containers while automatically recovering failed services and maintaining incident reports.

The project is built entirely on Ubuntu using Python and Docker to demonstrate practical DevOps concepts including Linux administration, monitoring, automation, containerization, incident management, and infrastructure reliability.

---

## Project Objectives

* Learn Linux and DevOps fundamentals through hands-on implementation
* Build a monitoring platform from scratch without relying on third-party monitoring software
* Understand infrastructure automation and self-healing systems
* Gain practical experience with Docker-based environments
* Develop production-oriented Python programming skills
* Showcase real DevOps engineering practices in a portfolio project

---

## Current Features

### System Monitoring

* CPU usage monitoring
* Memory utilization monitoring
* Disk usage monitoring
* Live system statistics using `psutil`

---

### Process Monitoring

Monitors important system processes such as:

* SSH
* Docker
* Python
* Chrome

Capabilities:

* Detect running processes
* Report process availability
* Verify essential services

---

### Network Monitoring

Performs infrastructure connectivity checks including:

* Internet connectivity verification
* DNS resolution
* Host availability checks
* IP address resolution

Monitored hosts include:

* Google
* GitHub

---

### Log Analysis Engine

Parses application logs to detect:

* Errors
* Warnings

Capabilities:

* Log parsing
* Error counting
* Warning counting
* Automatic report generation

Generated report:

```
reports/log_report.txt
```

---

### Docker Infrastructure

Creates a small production-like environment consisting of:

* Flask Application Container
* Nginx Container
* Redis Container

Capabilities:

* Build Docker images
* Deploy containers
* Monitor container status

---

### Container Monitoring

Automatically discovers active containers and reports:

* Running containers
* Missing containers
* Infrastructure status

---

### Self-Healing Recovery Engine

Detects stopped containers and performs automatic recovery.

Current workflow:

```
Container Failure
        │
        ▼
Failure Detection
        │
        ▼
Automatic Restart
        │
        ▼
Recovery Verification
        │
        ▼
Incident Report Generation
```

---

### Incident Reporting

Every recovery attempt is recorded in:

```
reports/incidents.txt
```

Each record contains:

* Timestamp
* Failed container
* Recovery status

---

### Modular Project Structure

The project has been refactored into a modular architecture for better scalability and maintainability.

```
self-healing-platform/

├── src/
│   ├── monitoring/
│   ├── recovery/
│   ├── alerts/
│   ├── config/
│   └── utils/
│
├── docker/
├── logs/
├── reports/
├── tests/
├── docs/
├── scripts/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Technologies Used

### Programming

* Python 3

### Operating System

* Ubuntu Linux

### Containerization

* Docker

### Version Control

* Git
* GitHub

### Linux Utilities

* Bash
* systemctl
* ps
* htop
* ping
* netstat
* ss
* grep
* tail
* tree

### Python Libraries

* psutil
* subprocess
* pathlib
* socket
* datetime

---

## DevOps Concepts Covered

* Linux Administration
* Process Monitoring
* Infrastructure Monitoring
* Network Monitoring
* Log Analysis
* Incident Management
* Self-Healing Systems
* Container Monitoring
* Docker Operations
* Infrastructure Automation
* Python Automation
* Modular Project Architecture

---

## Project Workflow

```
                 Ubuntu Host
                      │
                      ▼
             Monitoring Modules
      ┌──────────┬──────────┬──────────┐
      │          │          │          │
 System     Process     Network     Logs
Monitor     Monitor     Monitor    Parser
      │          │          │          │
      └──────────┴──────────┴──────────┘
                      │
                      ▼
            Docker Infrastructure
                      │
                      ▼
          Self-Healing Recovery Engine
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
 Incident Reports          Alert Module
```

---

## Running the Project

Clone the repository

```bash
git clone <repository-url>
cd self-healing-platform
```

Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the complete platform

```bash
python main.py
```

---

## Sample Output

```
===== SELF-HEALING PLATFORM =====

Running src.monitoring.monitor

CPU Usage: 18%
RAM Usage: 24%
Disk Usage: 12%

Running src.monitoring.process_checker

docker: RUNNING
ssh: RUNNING

Running src.monitoring.network_checker

google.com
DNS: OK

github.com
DNS: OK

Running src.monitoring.log_parser

Total Errors: 2
Total Warnings: 2

Running src.recovery.auto_recovery

Checking: nginx-demo

Status: RUNNING

===== ALL MODULES EXECUTED =====
```

---

## Future Improvements

Planned enhancements include:

* Web dashboard for infrastructure visualization
* Real-time metrics monitoring
* Email and Telegram alerts
* YAML-based configuration management
* CI/CD pipeline using GitHub Actions
* Systemd service integration
* Kubernetes deployment
* Prometheus integration
* Grafana dashboard
* REST API for infrastructure management
* Health check endpoints
* Multi-node monitoring
* Role-based authentication
* Database-backed incident history
* Unit and integration tests

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Python scripting for DevOps
* Linux system administration
* Bash command-line utilities
* Docker container management
* Infrastructure monitoring
* Process management
* Network diagnostics
* Log parsing
* Automation
* Self-healing infrastructure design
* Git and GitHub workflows
* Modular software architecture

---

## Repository Status

**Current Stage:** Active Development

The project is under continuous development with new DevOps features and production-grade improvements being added incrementally.

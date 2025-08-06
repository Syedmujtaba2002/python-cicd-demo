# Python Flask CI/CD with Jenkins, Docker, and GitHub Webhooks

This project demonstrates a complete CI/CD pipeline for a Python Flask application using Jenkins, Docker, and GitHub.

---

## Overview

The objective of this project is to automate the process of building, testing, and deploying a Python Flask web application using Jenkins CI/CD pipeline. The pipeline is initially triggered through SCM polling and later enhanced with a GitHub webhook for automatic builds on every push.

---

## Environment Used

- OS: Ubuntu
- CI Tool: Jenkins
- Source Control: Git & GitHub
- Language: Python (Flask)
- Containerization: Docker

---

## Process Followed

### 1. Jenkins Installation (on Ubuntu)

Jenkins was installed on an Ubuntu server using official instructions. Required plugins like Git, Pipeline, Docker Pipeline, and GitHub Integration were installed.



### 2. Manual Pipeline Build

Once the Jenkinsfile and project were set up, a manual build was triggered to ensure all stages (`build`, `test`, and `deploy`) executed successfully. The application was packaged in a Docker container and deployed.

### 3. GitHub Webhook Integration

After confirming the pipeline worked manually:
- A **GitHub webhook** was added, pointing to Jenkins at `/github-webhook/`
- Jenkins was configured to trigger builds using **"GitHub hook trigger for GITScm polling"**

This allowed automatic triggering of the Jenkins pipeline on every push to the GitHub repository.

### 4. Final Testing

A test commit was pushed to the GitHub repository. The webhook triggered Jenkins automatically, running the complete pipeline without manual intervention. The deployed Flask app was then verified by accessing it via the public IP on port 5000.

---

## Outcome

This setup provides a complete CI/CD solution for a Python web app, from source code push to automated testing and deployment via Docker, all managed through Jenkins.

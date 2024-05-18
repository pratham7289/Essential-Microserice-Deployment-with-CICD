# -Essential-Microservices-Deployment-with-CI-CD

## Introduction
The Task Management System is a Python and Flask-based application designed to facilitate efficient task management for users. It allows users to register, log in, and log out to access their task lists. The system offers functionalities for adding, updating, and deleting tasks.

## System Architecture
The system architecture is built using the following technologies:
- **Backend**: Python with Flask framework, chosen for its simplicity, flexibility, and robustness in building applications.
- **Containerization**: Docker for creating lightweight, portable containers, ensuring consistency across different environments and simplifying deployment.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Jenkins for automating the build and deployment process, streamlining the development lifecycle and ensuring rapid and reliable delivery of updates.
- **Container Orchestration**: Kubernetes (Minikube) for managing containerized applications.
- **Monitoring**: Prometheus collects metrics, and Grafana visualizes them, enabling real-time monitoring and performance analysis to maintain system health and optimize operations.

## Installation and Deployment
Follow these steps to set up and deploy the Task Management System:
1. **Clone Repository**: Clone the project repository from GitHub.
2. **Setup Environment**: Install Python, Flask, Docker, and Jenkins on your local machine or server.
3. **Configuration**:
    - Configure Jenkins with the GitHub repository and set up webhooks for automatic triggers.
    - Set up credentials in Jenkins Credential Manager for securely storing Docker Hub credentials.
    - Configure Docker Hub credentials in Jenkins using Credential Manager for pushing Docker images.
4. **Deployment**:
    - Build Docker images for the Flask application using Jenkins.
    ```bash
    docker build -t user-service -f Dockerfile.User .
    docker build -t task-service -f Dockerfile.Task .
    ```
    - Tag the Docker images.
    ```bash
    docker tag dockerfile.user ${env.dockerhubUser}/dockerfile.user:latest
    ```
    - Push Docker images to Docker Hub securely using the configured credentials.
    ```bash
    docker push ${env.dockerhubUser}/dockerfile.user:latest
    docker push ${env.dockerhubUser}/dockerfile.task:latest
    ```
    - Apply Jenkinsfile for deploying the application using Jenkins pipelines.
    - Apply Kubernetes YAML files for deploying the application to Minikube.
    ```bash
    kubectl apply -f User_Deployment.yml
    kubectl apply -f User_Service.yml
    kubectl apply -f Task_Deployment.yml
    kubectl apply -f Task_Service.yml
    ```

## Access Microservices
Access the microservices using their respective endpoints:
- User Service: [http://localhost:30001](http://localhost:30001) (or use NodePort assigned by Kubernetes)
- Task Service: [http://localhost:30002](http://localhost:30002) (or use NodePort assigned by Kubernetes)

## Monitoring Jenkins Pipeline with Prometheus and Grafana
### Prerequisites
- Jenkins installed and running.
- Prometheus and Grafana installed and accessible.

### Step 1: Install Prometheus
Follow the installation instructions provided in the official Prometheus documentation.

### Step 2: Install Grafana
Follow the installation instructions provided in the official Grafana documentation.

### Step 3: Configure Data Sources in Grafana
- Access Grafana dashboard using its URL.
- Log in using your credentials.
- Add Prometheus as a data source using Prometheus service IP and port.

### Step 4: Import Default Dashboards
- Click on "Dashboards" -> "Manage" -> "Import".
- Use the dashboard ID for Jenkins monitoring to import the default Jenkins monitoring dashboard.

### Step 5: Access Jenkins Metrics
- Access Jenkins metrics endpoint using the appropriate URL.
- Explore available metrics related to Jenkins pipeline execution and performance.

## Conclusion
Overall, this project demonstrates the power of modern DevOps tools and practices in building, deploying, and monitoring microservices-based applications. By following the documentation and utilizing the provided resources, users can replicate and extend this project to meet their own task management needs, driving efficiency and productivity in their organizations.

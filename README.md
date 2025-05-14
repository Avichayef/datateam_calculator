# Calculator App with Jenkins CI/CD

This project contains a calculator application with an automated CI/CD pipeline using Jenkins.
The setup includes containerized Jenkins with Docker capabilities and automated Python testing.

## Directory Structure
app/                   # Calculator application
tests/                 # Test files
Dockerfile             # App Dockerfile
Dockerfile.jenkins     # Jenkins Dockerfile (include plugins install)
docker-compose.yml     # Services configuration
Jenkinsfile            # Pipeline definition
requirements.txt       # Python dependencies

## Prerequisites

- Docker and Docker Compose installed
- Git installed
- Docker Hub account (for image pushing)

## Jenkins Setup

1. Clone this repository:
```bash
git clone https://github.com/Avichayef/datateam_calculator
cd datateam_calculator
```

2. Start Jenkins using Docker Compose:
```bash
docker-compose up -d jenkins
```

This will:
- Build a custom Jenkins container with Docker support
- Start Jenkins on port 8080
- Mount necessary volumes for persistence
- Configure Jenkins with root access for Docker operations

3. Access Jenkins:
- Open `http://localhost:8080` (or http://<VM IP>:8080) in browser
- Jenkins is configured to skip the setup wizard (`jenkins.install.runSetupWizard=false`)

## Jenkins Configuration

### Docker Hub Credentials Setup

1. Go to "Manage Jenkins" → "Credentials"
2. Click on "System" under Stores scoped to Jenkins
3. Click "Global credentials"
4. Click "Add Credentials"
5. Select "Username with password"
6. Set the following:
   - Kind: Username with password
   - Scope: Global
   - Username: <Docker Hub username>
   - Password: <Docker Hub password>
   - ID: dockerhub-credentials
   - Description: Docker Hub Credentials

### Pipeline Setup

1. In Jenkins dashboard, click "New Item"
2. Enter a name ("calculator-pipeline")
3. Select "Pipeline"
4. In configuration:
   - Under "Pipeline", select "Pipeline script from SCM"
   - Select "Git" as SCM
   - Enter https://github.com/Avichayef/datateam_calculator
   - Set "Script Path" to "Jenkinsfile" and save

## Pipeline Stages

The pipeline consists of 3 stages:

1. **Test**
   - Runs in Python 3.13-slim container
   - Installs requirements
   - Executes pytest
   - Generates JUnit test reports

2. **Build Docker Image**
   - Builds calculator app image
   - Tags with build number and 'latest'

3. **Push to Docker Hub**
   - Log in to Docker Hub
   - Pushes images with version and 'latest' tags


## ------------------------------------------------------------------------------------ ##

## Docker Compose Services

### Calculator Service
- Builds from project Dockerfile
- Mounts current directory
- Runs pytest with JUnit XML output

### Jenkins Service
- Custom build from Dockerfile.jenkins
- Exposed ports:
  - 8080 (Web UI)
  - 50000 (Agent communication)
- Volumes:
  - jenkins_home (persistence)
  - docker.sock (Docker access)

## Environment Variables

The pipeline uses:
- `PYTHON_IMAGE`: python:3.13-slim
- `BUILD_NUMBER`: Jenkins build number (automatic)
- `DOCKER_USERNAME`: Docker Hub username (from credentials)
- `DOCKER_PASSWORD`: Docker Hub password (from credentials)

## Test Reports

- JUnit test reports are automatically collected
- Available in Jenkins build results
- Failed tests will mark the build as failed



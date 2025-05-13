pipeline {
    agent any  // run on the main node with Docker access

    environment {
        PYTHON_IMAGE = 'python:3.13-slim'
    }

    stages {
        stage('Test') {
            steps {
                // Run tests inside the Python container
                script {
                    docker.image(env.PYTHON_IMAGE).inside {
                        sh 'pip install -r requirements.txt'
                        sh 'python -m pytest tests/ --junitxml=test-results.xml'
                    }
                }
            }
            post {
                always {
                    // Archive test results
                    junit 'test-results.xml'
                }
                failure {
                    echo 'UnitTests failed!'
                }
            }
        }


        stage('Build Docker Image') {
            steps {
                // Build Docker image for calculator app
                sh 'docker build -t calculator-app:${BUILD_NUMBER} .'  // Build image with build num as tag
                sh 'docker tag calculator-app:${BUILD_NUMBER} calculator-app:latest'  // Also tag the last one as 'latest'
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', 
                                                 usernameVariable: 'DOCKER_USERNAME', 
                                                 passwordVariable: 'DOCKER_PASSWORD')]) {
                    // Login to Docker Hub
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    
                    // Tag image with username
                    sh 'docker tag calculator-app:latest $DOCKER_USERNAME/calculator-app:latest'
                    
                    // Push image to Docker Hub
                    sh 'docker push $DOCKER_USERNAME/calculator-app:latest'
                    
                    // Also push versioned tag
                    sh 'docker tag calculator-app:${BUILD_NUMBER} $DOCKER_USERNAME/calculator-app:${BUILD_NUMBER}'
                    sh 'docker push $DOCKER_USERNAME/calculator-app:${BUILD_NUMBER}'
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully! The calculator app has been tested, built, and is ready for deployment.'
        }
        failure {
            echo 'Pipeline failed. Please check the logs and test reports.'
        }
    }
}

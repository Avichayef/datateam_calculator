pipeline {
    agent {
        // Specify where pipeline will execute
        docker {
            image 'python:3.13-slim'  // execution environment
        }
    }
    
    stages {
        stage('Setup') {
            steps {
                // Install Python dependencies
                sh 'pip install -r requirements.txt'  // pip install packages from requirements.txt
            }
        }
        
        stage('Test') {
            steps {
                // Run the tests
                sh 'python -m pytest tests/ --junitxml=test-results.xml'  // Runs pytest and generates XML output
            }
            post {
                always {
                    junit 'test-results.xml'  // process and display the test results (always, even if fails)
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

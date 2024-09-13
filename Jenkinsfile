pipeline {
    agent any
    environment {
        // Specify your Docker image name
        DOCKER_IMAGE = 'flask-crud-app'
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from GitHub
                git branch: 'main', url: 'https://github.com/Nachiket-D/Flask-To-Do-List-Project.git'
            }
        }
        stage('Build') {
            steps {
                // Build Docker image for Flask app using sudo
                script {
                    sh "sudo docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }
        stage('Run') {
            steps {
                // Run Docker container using sudo
                script {
                    sh "sudo docker run -d -p 5000:5000 ${DOCKER_IMAGE}"
                }
            }
        }
    }
    post {
        always {
            // Clean up containers after the pipeline finishes using sudo
            sh 'sudo docker container prune -f'
        }
    }
}

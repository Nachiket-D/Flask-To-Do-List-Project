pipeline {
    agent any
    environment {
        // Specify your Docker image name
        DOCKER_IMAGE = 'flask-crud-app'
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from a version control system (e.g., GitHub)
                git branch: 'main', url: 'https://github.com/Nachiket-D/Flask-To-Do-List-Project.git'
            }
        }
        stage('Build') {
            steps {
                // Build Docker image for Flask app
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }
        stage('Run') {
            steps {
                // Run Docker container
                script {
                    docker.image("${DOCKER_IMAGE}").run('-d -p 5000:5000')
                }
            }
        }
    }
    post {
        always {
            // Optional: Clean up containers after the pipeline finishes
            sh 'docker container prune -f'
        }
    }
}

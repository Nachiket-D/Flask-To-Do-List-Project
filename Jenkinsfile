pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t my-flask-app .'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    // Remove the existing container if it exists
                    sh 'docker stop my-flask-app || true && docker rm my-flask-app || true'

                    // Run the new container
                    sh 'docker run -d -p 5000:5000 --name my-flask-app my-flask-app'
                }
            }
        }
    }
}

# Flask To-Do List Project

This project allows you to create a to-do list using Python Flask, Docker, HTML, and CSS.

## Prerequisite

Before cloning the project, ensure that Docker is installed on your local machine. You can download Docker [here](https://www.docker.com/products/docker-desktop).

## Getting Started

### Cloning the Project

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-repository-url/flask-to-do-list.git
   cd flask-to-do-list
   ```

### Running the Project with Docker

1. Build the Docker image:
   ```bash
   docker build -t flask-todo-app .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 5000:5000 flask-todo-app
   ```

3. Open your browser and navigate to `http://localhost:5000` to access the application.

## Setting Up Jenkins 

If your repository has a Jenkinsfile, follow these steps to set up a Jenkins pipeline:

### 1. Install Jenkins

You can install Jenkins by following the [Jenkins installation guide](https://www.jenkins.io/doc/book/installing/).

### 2. Set Up Jenkins

Once Jenkins is installed, create a new pipeline:

1. Open Jenkins in your browser (`http://localhost:8080` if running locally).
2. Log in using your Jenkins credentials.
3. Click on **New Item**, enter a name for the pipeline, select **Pipeline**, and click **OK**.
4. Under **Pipeline**, in the **Pipeline script from SCM** section, select **Git**.
5. In the **Repository URL**, enter your repository URL where the Jenkinsfile is located.
6. Select the branch you want to build (e.g., `main` or `master`).
7. Click **Save**.

### 3. Triggering the Pipeline

Once the pipeline is set up:

1. Every time you push code to the repository, Jenkins will automatically trigger a build, provided your repository includes a valid `Jenkinsfile`.


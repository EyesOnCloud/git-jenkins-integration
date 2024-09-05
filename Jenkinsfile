pipeline {
    agent any
    environment {
        // Replace 'ssh-git-credentials' with your actual Jenkins credentials ID for the SSH key
        GIT_SSH_CREDENTIALS = credentials('git-credentials')
    }
    stages {
        stage('Clone Repository') {
            steps {
                // Use SSH credentials to clone the repository
                git branch: 'master', 
                    url: 'git@github.com:EyesOnCloud/git-jenkins-integration.git',
                    credentialsId: 'git-credentials'
            }
        }
        stage('Set Up Python Environment') {
            steps {
                script {
                    sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    '''
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt || echo "No requirements file"'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh 'python -m unittest discover'
                }
            }
        }
    }
    post {
        always {
            echo 'Build finished'
        }
        success {
            echo 'Build successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}

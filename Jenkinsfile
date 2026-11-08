pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '.venv/bin/pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                        -t devops-dashboard:${BUILD_NUMBER} .
                '''
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Investigate the failed stage.'
        }
    }
}

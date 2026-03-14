pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo "Cloning repository..."
                git branch: 'main', url: 'https://github.com/yash15808/cineops-devops.git'
            }
        }

        stage('Trivy Scan Terraform') {
            steps {
                echo "Running Terraform security scan..."
                sh '''
                cd terraform
                docker run --rm \
                -v $(pwd):/workspace \
                aquasec/trivy:latest config /workspace
                '''
            }
        }


        stage('Terraform Plan') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'aws-credentials',
                    usernameVariable: 'AWS_ACCESS_KEY_ID',
                    passwordVariable: 'AWS_SECRET_ACCESS_KEY'
                )]) {
                    sh '''
                    export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
                    export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
                    export AWS_DEFAULT_REGION=us-east-1

                    cd terraform
                    terraform init
                    terraform plan
                    '''
                }
            }
        }

    }
}

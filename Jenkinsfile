pipeline {

    agent any

    stages {

        stage('Clone Repository') {

            steps {

                echo 'Repository Ready'

            }

        }

        stage('Build Docker Image') {

            steps {

                bat 'docker build -t devops-control-center Backend'

            }

        }

        stage('Stop Old Container') {

            steps {

                bat 'docker stop devops-dashboard || exit 0'

                bat 'docker rm devops-dashboard || exit 0'

            }

        }

        stage('Run New Container') {

            steps {

                bat 'docker run -d -p 5000:5000 --name devops-dashboard devops-control-center'

            }

        }

    }

}
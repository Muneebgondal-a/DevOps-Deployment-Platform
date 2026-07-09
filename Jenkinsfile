pipeline {

    agent any

    stages {

        stage('Repository Ready') {

            steps {

                echo 'Repository Ready'

            }

        }

        stage('Check Docker') {

            steps {

                sh 'docker --version'

            }

        }

        stage('Build Docker Image') {

            steps {

                sh 'docker build -t devops-control-center Backend'

            }

        }

        stage('Stop Old Container') {

            steps {

                sh 'docker stop devops-dashboard || true'

                sh 'docker rm devops-dashboard || true'

            }

        }

        stage('Run New Container') {

            steps {

                sh 'docker run -d -p 5000:5000 --name devops-dashboard devops-control-center'

            }

        }

    }

}
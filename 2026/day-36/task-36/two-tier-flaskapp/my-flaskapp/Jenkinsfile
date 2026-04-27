@Library('Shared') _
pipeline {
    agent {label "dev"};

    stages {
        stage("Code") {
            steps {
                script{
                clone("https://github.com/nilesh-fatfatwale/two-tier-flask-app", "main")
                }
            }
        }
        stage("Trivy file system scan") {
              steps {
                 script{
                     trivy_fs()
                 }
              }
            }
            
        stage("Build") {
            steps {
                sh "docker build -t flask-app:latest ."
            }
        }

        stage("Test") {
            steps {
                echo "code is testing"
            }
        }

        stage("Push to Docker Hub") {
            steps {
                script{
                    docker_push("dockerHubCreds","flask-app")
                }
            }
        }

        stage("Run") {
            steps {
                sh "docker compose up -d --build flask-app"
            }
        }
    }
    post{
        success{
            script{
                emailext from: 'fatfatwalenilesh@gmail.com',
                to : 'yehmerifakeidhai@gmail.com',
                body : 'Build Success',
                subject : 'Build Success'
            }
        }
        failure{
            script{
            emailext from : 'fatfatwalenilesh@gmail.com',
            to : 'yehmerifakeidhai@gmail.com',
            body : 'Build failed',
            subject : 'Build failed'
            }
        }
    }
}

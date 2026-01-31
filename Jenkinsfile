pipeline {
    agent any

    environment {
        VENV = ".venv"
    }

    triggers {
        cron('H/5 * * * *') // Runs every 5 minutes
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/ArunHonnappa-1/BlogPost'
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Setting up virtual environment and installing dependencies...'
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'

                script {
                    if (fileExists('requirements.txt')) {
                        bat '.venv\\Scripts\\pip install -r requirements.txt'
                    } else {
                        echo 'No requirements.txt found, installing pytest only.'
                        bat '.venv\\Scripts\\pip install pytest pytest-html'
                    }
                }

                // Create reports folder safely
                bat 'if not exist reports mkdir reports'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running test cases...'
                bat '.venv\\Scripts\\python.exe -m pytest --html=reports\\report.html --self-contained-html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Test Report'
                ])
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Email notification skipped.'
        }
    }
}

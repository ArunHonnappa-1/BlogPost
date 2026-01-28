pipeline {
    agent any

    environment {
        VENV = ".venv"
    }

    triggers {
        cron('H * * * *') // Runs every hour
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
                bat "python -m venv %VENV%"
                bat "%VENV%\\Scripts\\pip install --upgrade pip"
                bat "%VENV%\\Scripts\\pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running test cases...'
                bat "%VENV%\\Scripts\\pytest --html=reports\\report.html --self-contained-html"
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    allowMissing: false,
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
            echo 'Sending email notification...'
            emailext (
                subject: "Automation Test Report",
                body: "Please check attached automation report.",
                to: "arunh202@gmail.com",
                attachLog: true
            )
        }
    }
}


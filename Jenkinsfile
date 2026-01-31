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
                bat '.venv\\Scripts\\pip install -r requirements.txt'
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
                subject: "Automation Test Report - Build #${BUILD_NUMBER}",
                body: """Hi Team,

Please find the automation test report attached.

Job: ${JOB_NAME}
Build: ${BUILD_NUMBER}
Status: ${BUILD_STATUS}
URL: ${BUILD_URL}""",
                to: "arunh202@gmail.com",
                attachmentsPattern: 'reports/report.html', // <-- Correct for Pipeline
                attachLog: true
            )
        }
    }
}

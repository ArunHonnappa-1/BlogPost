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

                // Install dependencies if requirements.txt exists
                script {
                    if (fileExists('requirements.txt')) {
                        bat '.venv\\Scripts\\pip install -r requirements.txt'
                    } else {
                        echo 'No requirements.txt found, skipping dependency installation.'
                    }
                }

                // Create reports folder to avoid pytest errors
                bat 'mkdir reports'
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
            echo 'Pipeline finished. Email notification skipped.'

//             // Use Jenkins built-in mail step (no attachment support)
//             mail(
//                 to: 'arunh202@gmail.com',
//                 subject: "Automation Test Report - Build #${BUILD_NUMBER}",
//                 body: """Hi Team,

// Please find the automation test report link below:

// Job: ${JOB_NAME}
// Build: ${BUILD_NUMBER}
// Status: ${currentBuild.currentResult}
// URL: ${BUILD_URL}

// Note: Report attachment not supported in this setup."""
//             )
        }
    }
}

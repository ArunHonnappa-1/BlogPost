pipeline {
    agent any

    environment {
        VENV = ".venv"
    }

    triggers {
        cron('H/5 * * * *')
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/ArunHonnappa-1/BlogPost'
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Setting up virtual environment...'
                bat 'python -m venv %VENV%'
                bat '%VENV%\\Scripts\\python.exe -m pip install --upgrade pip'

                script {
                    if (fileExists('requirements.txt')) {
                        echo 'Installing dependencies from requirements.txt'
                        bat '%VENV%\\Scripts\\pip install -r requirements.txt'
                    } else {
                        echo 'No requirements.txt found. Installing basic test packages.'
                        bat '%VENV%\\Scripts\\pip install pytest pytest-html selenium'
                    }
                }

                bat 'if not exist reports mkdir reports'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running test cases...'
                bat '%VENV%\\Scripts\\python.exe -m pytest --html=reports\\report.html --self-contained-html'
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
            echo 'Pipeline finished.'
        }
    }
}

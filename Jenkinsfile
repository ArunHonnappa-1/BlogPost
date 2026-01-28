pipeline {
    agent any

    environment {
        VENV = ".venv"
        REPORT_DIR = "reports"
    }

    stages {

        stage('Setup Python') {
            steps {
                echo "Setting up virtual environment and installing dependencies..."
                sh 'python -m venv ${VENV}'
                sh '${VENV}/bin/pip install --upgrade pip'
                sh '${VENV}/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo "Creating reports folder if missing..."
                sh "mkdir -p ${REPORT_DIR}"

                echo "Running Selenium tests..."
                sh "${VENV}/bin/pytest TestCases/ --html=${REPORT_DIR}/report.html --self-contained-html"
            }
        }

        stage('Publish Report') {
            steps {
                echo "Publishing HTML test report..."
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: "${REPORT_DIR}",
                    reportFiles: 'report.html',
                    reportName: 'Selenium Automation Report'
                ])
            }
        }
    }

    post {
        always {
            echo "Sending email notification..."

            // Email notification
            emailext (
                subject: "Selenium Automation Test Report",
                body: "Please check attached automation report.",
                to: "arunh202@gmail.com",
                attachLog: true
            )
        }
    }
}

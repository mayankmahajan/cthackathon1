pipeline {
agent {label 'mac'}
  environment {
        ARTIFACTS_PATH = 'target/artifacts/'
        PYPI_SERVER = 'http://192.168.192.201:5050/'
        NIMBLE = 'nimble'
        FILESERVER_PASSWORD = 'Gu@vu\\$12#'
        FILESERVER_DESTINATION = '/var/www/html/guavus/automation/validation'
  }
  stages {


        stage("virtual environment") {

            steps {
                sh ""
            }
        }

        stage("Challenge0") {

            steps {
                sh "source ~/py3env/bin/activate && cd testautomationcode && python -m pytest tests/ && deactivate"
            }
        }
  }

  post {
        always {
            script {
                allure includeProperties: false, jdk: '', results: [[path: "target/artifacts/allure/"]]
            }
       }
  }
}
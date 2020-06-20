pipeline {
agent {label 'mac'}
  environment {
        ARTIFACTS_PATH = 'target/artifacts/'
        PYPI_SERVER = 'http://192.168.192.201:5050/'
        NIMBLE = 'nimble'
        FILESERVER_PASSWORD = 'Gu@vu\\$12#'
        FILESERVER_DESTINATION = '/var/www/html/guavus/automation/validation'
  }
  stage("Build Test Docker"){
            agent {
                docker { image 'python:3-alpine'
                         args '-e HOME=$WORKSPACE'
                         reuseNode true
                }
            }

      stages {
            stage("virtual environment") {

                steps {
//                     sh "pip install virtualenv"
//                     sh "virtualenv py3env -p python3 && source ~/py3env/bin/activate && cd testautomationcode && pip install requirements.txt && deactivate"
                    sh "cd testautomationcode && pip install requirements.txt"
                }
            }

            stage("Challenge0") {

                steps {
                    sh "cd testautomationcode && python -m pytest tests/"
                }
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
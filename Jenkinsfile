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



        stage("Push docker images in artifactory") {

            steps {
                echo "Run Commmand to push docker image in artifactory"
            }
        }
  }

  post {
        always {
            script {
                sh "echo Hi."
            }
       }
  }
}
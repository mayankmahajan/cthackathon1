pipeline {
agent {label 'any'}
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
                // sh 'docker push artifacts.ggn.in.guavus.com:4244/${NIMBLE}:${dockerTag}'
                docker_push( env.buildType, env.NIMBLE )
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
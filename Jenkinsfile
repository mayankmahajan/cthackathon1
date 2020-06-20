pipeline {
    agent {label 'mac'}
      environment {
            BASEURL = 'http://35.188.114.237:8088/'
      }
  stages {

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
                        sh "cd testautomationcode && pip install -r requirements.txt"
                    }
                }

                stage("Challenge0") {

                    steps {
                        sh "cd testautomationcode && python -m pytest tests/"
                    }
                }
      }
  }
  }

  post {
            always {
                script {
                    echo "post action"
//                     allure includeProperties: false, jdk: '', results: [[path: "target/artifacts/allure/"]]
                }
           }
  }
}
pipeline {
  environment {
    registry = "mguazzardo/curso-jenkins"
    registryCredential = 'dockerhub'
  }
 agent any
  stages {

    stage('Build Docker Image') {
            steps {
                script {
                    app = docker.build("mguazzardo/flaskapi:latest")
                }
            }
        }

   stage('Run Container') {
      steps{
        
        sh '''
        docker run -d --name=flaskapi -p 30080:5000 mguazzardo/flaskapi
        
           '''
        }
      }

    stage('Test Container') {
      steps{

        sh '''
        chmod +x curl_test.sh
        ./curl_test.sh
        sleep 5
        docker rm -f flaskapi

           '''
        }
      }


    


   stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
    

    
    
    }   


}

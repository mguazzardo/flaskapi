pipeline {
  environment {
    registry = "mguazzardo/curso-jenkins"
    registryCredential = 'dockerhub'
  } 
 agent any  
  stages {
    stage('Building image') {
      steps{
        script {
          //docker.build registry + ":$BUILD_NUMBER" // Cambio para que pueda pushear con groovy
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    } // fin del stage
   stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( 'https://index.docker.io/v1/', registryCredential ) {
                dockerImage.push("$BUILD_NUMBER")
          }
          sh '''
          docker run -d --name=flaskapi -p 5000:5000 mguazzardo/curso-jenkins:8
          '''
          
        }
      }
    }
    
  }//stages
}//pipeline

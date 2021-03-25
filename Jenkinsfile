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
          sleep 120
          docker run -d --name=php-test -p 5000:5000 php-test-app
          '''
          
        }
      }
    }
    
  }//stages
}//pipeline

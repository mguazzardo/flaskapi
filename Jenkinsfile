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
      
          sh '''
          docker run -d --name=flaskapi -p 5000:5000 mguazzardo/curso-jenkins:$BUILD_NUMBER
          
          '''
          
      }//steps
    } //stage
    
    stage('Upload Image') {
      steps{
        script {
          docker.withRegistry( 'https://index.docker.io/v1/', registryCredential ) {
            //Poner con groovy

          }
          sh '''
          #docker push mguazzardo/curso-jenkins:$BUILD_NUMBER
             '''
        }
      }
    }
    
    
  }//stages
}//pipeline

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
   stage('Deploy and Test Image') {
      steps{
          
          sh '''
          chmod +x ./test.sh
          ./test.sh
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
    
    
    
    stage('Deploy to k8s') {
      steps{
          sh '''
          #docker push mguazzardo/curso-jenkins:$BUILD_NUMBER
          #ssh 172.17.0.1 kubectl create deployment flaskapi --image=mguazzardo/flaskapi -n flaskapi
             '''
        
      }
    }
    
  }//stages
}//pipeline

pipeline {
  environment {
    registry = "santhoshchanda/helloworld"
    registryCredential = 'dockerhub'
    dockerImage = ''
    ecrregistry= '420407463971.dkr.ecr.us-east-2.amazonaws.com/helloworld'
    ecrregistryCredential= 'aj_user'
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git branch: 'integrate_ecr', url: 'https://github.com/santhoshchanda/helloworld.git'
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
      steps{
         script {
            docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
	      }
      }
    }
       stage('Deploy Image to ECR') {
      steps{
         script {
            docker.withRegistry( "https://" + ecrregistry, "ecr:eu-central-1:" + ecrregistryCredential ) {
            dockerImage.push()
          }
	      }
      }
    } 
  }
}


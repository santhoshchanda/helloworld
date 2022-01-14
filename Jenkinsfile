pipeline {
  environment {
    registry = "santhoshchanda/helloworld"
    registryCredential = 'dockerhub'
    dockerImage = ''
    ecrregistry= 'public.ecr.aws/a6j1m8o6/helloworldpub'
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
            docker.withRegistry( "https://" + ecrregistry, ecrregistryCredential ) {
            dockerImage.push()
          }
	      }
      }
    } 
  }
}


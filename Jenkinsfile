#!groovy
pipeline{
    agent any
    stages{
        stage('Preparation'){
            steps{
                sh 'hostname'
                sh 'id'
                sh 'pwd'
            }
        }
        stage('Checkout'){
            steps{
                sh 'touch $RELEASE'
            }
        }
    }
}

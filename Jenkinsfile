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
        stage('Build'){
            steps{
                echo 'I only execute on master branch'
                sh 'touch $RELEASE'
            }
        }
    }   
}

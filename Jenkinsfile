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
            if (env.BRANCH_NAME == 'master'){
                echo 'I only execute on master branch'
                steps{
                    sh 'touch $RELEASE'
                }
            }
        }
    }
}

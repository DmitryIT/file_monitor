#!groovy
pipeline{
    agent any
    environment{
        PROJECT = 'file_monitor'
    }
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
                sh  'tar -czvf ${PROJECT}_${RELEASE}.tar.gz .'
                print 'archive ${PROJECT}_${RELEASE}.tar.gz created'

            }
        }
    }
    post{
        always{
            echo 'I\'m finished. Removing Workspace...'
            //deleteDir()
        }
    }   
}

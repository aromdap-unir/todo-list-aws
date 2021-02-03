pipeline {
    agent any
    stages {
        stage('Clean'){    
            steps {
                deleteDir()
                sh 'printenv'
            }
        }
        stage('SetUp'){
            steps{
                // Setup Virtualenv for testing
                echo 'SetUp >> Creating Python Virtual Environment'
                sh "pip3 install virtualenv"
                sh "virtualenv -p /usr/bin/python3.7 venv"
                sh "source venv/bin/activate"
            }
        }
    }       
}

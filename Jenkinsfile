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
                sh "python3 -m venv env"
                sh "source env/bin/activate"
                sh "which python3.7"
                sh "pip3 install -r requirements.txt"
            }
        }
    }       
}

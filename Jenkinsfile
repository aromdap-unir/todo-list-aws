pipeline {
    agent any
    stages {
        stage('Clean'){    
            steps {
                echo 'Clean >> Environmental variables'
                deleteDir()
            }
        }
        stage('Checkout') {
            steps {
                // Get some code from a CodeCommit repository
                git branch: 'dev', credentialsId: '676655fc-c40f-4964-b3ba-c3dfb91b2094', url: 'https://git-codecommit.us-east-1.amazonaws.com/v1/repos/todo-list-aws'
                sh 'ls -lh'
            }
        }
        stage('SetUp'){
            steps{
                // Setup Virtualenv for testing
                echo 'SetUp >> Creating Python Virtual Environment'
                sh '''
                    python3 -m venv env
                    source env/bin/activate
                    which python3.7
                    pip install -r requirements.txt
                '''
            }
        }
        stage('GoodPractices'){
            steps{
                // Setup Virtualenv for testing
                echo 'GoodPractices >> Static analysis of code'
                sh '''
                    source env/bin/activate
                    radon cc src/
                    flake8 src/
                '''
            }
        }
    }       
}

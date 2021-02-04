pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                deleteDir()
                echo '// Checkout // Get some code from a CodeCommit repository'
                git branch: 'dev', credentialsId: '676655fc-c40f-4964-b3ba-c3dfb91b2094', url: 'https://git-codecommit.us-east-1.amazonaws.com/v1/repos/todo-list-aws'
                sh '''
                    ls -lh
                    printenv
                '''
            }
        }
        stage('SetUp'){
            steps{
                // Setup Virtualenv for testing
                echo '// SetUp // Creating Python Virtual Environment'
                sh '''
                    python3 -m venv env
                    source env/bin/activate 
                    which python3.7
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Testing'){
            steps{
                echo '// Testing // Static analysis of code'
                sh '''
                    rm ./radon/*
                    rm ./flake8/*
                    source env/bin/activate
                    
                    radon cc src/ --min B --total-average -s --json --output-file ./radon/analysis.json
                    cat ./radon/analysis.json
                    grep -il 'rank' ./radon/* && echo 'Radon test: failed' || echo 'Radon test: passed!'
                    
                    flake8 src/ --exit-zero --ignore W --statistics --show-source --format=pylint --output-file ./flake8/analysis.json
                    cat ./flake8/analysis.json
                    grep -il -E '[[:alnum:]]' ./flake8/* && echo 'Flake8 test: failed' || echo 'Flake8 test: passed!'
                    
                '''

            }
        }
        
        stage('Deploy'){
            steps{
                echo '// Testing // Unittesting of source code'
                sh '''
                    source env/bin/activate
                    
                '''
            }
        }
    }       
}

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                deleteDir()
                echo '// Checkout // Get some code from a CodeCommit repository'
                git branch: 'dev', credentialsId: '676655fc-c40f-4964-b3ba-c3dfb91b2094', url: 'https://git-codecommit.us-east-1.amazonaws.com/v1/repos/todo-list-aws'
                sh 'ls -lh'
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
                    radon cc src/ --min B --total-average -s --json --output-file ./radon/cc_analysis.json
                    grep -ril "rank" ./radon && error('Aborting the build: radon detected low quality >> REVIEW CODE')
                    flake8 --statistics src/ --show-source --ignore=W293 --format=pylint --output-file ./flake8/analysis.json
                    grep -ril "\[W" ./flake8 && error('Aborting the build: flake8 detected PEP8 errors >> REVIEW CODE')
                '''

                echo '// Testing // Security analysis of code'
                sh '''
                    rm ./radon/*
                    rm ./flake8/*
                    source env/bin/activate
                    radon cc src/ --total-average -s --json --output-file ./radon/cc_analysis.json 
                    radon raw src/ --summary --json --output-file ./radon/raw_analysis.json
                    flake8 --statistics src/ --show-source --ignore=W293 --format=pylint --output-file ./flake8/analysis.json
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

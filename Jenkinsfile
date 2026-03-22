pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning code...'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
                echo 'installing  dependencies ......'
            }
        }

        stage('Run Producer') {
            steps {
                bat 'python producer/app.py'
            }
        }
    }
}

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
                bat '"C:/Users/amrut/AppData/Local/Programs/Python/Python313/python.exe" -m pip install --upgrade pip'
                bat '"C:/Users/amrut/AppData/Local/Programs/Python/Python313/python.exe" -m pip install -r requirements.txt'
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

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo '🔧 Creating virtual environment and installing dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests in virtualenv...'
                sh '''
                    . venv/bin/activate
                    pytest test_app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying Docker container...'
                script {
                    docker.build('python-cicd-demo')
                    sh 'docker run -d -p 5000:5000 python-cicd-demo'
                }
            }
        }
    }
}

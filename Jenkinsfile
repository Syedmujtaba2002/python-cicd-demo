pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo '🔨 Build Stage: Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Test Stage: Running unit tests...'
                sh 'pytest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploy Stage: Building and running Docker container...'
                script {
                    docker.build('python-cicd-demo')
                    sh 'docker run -d -p 5000:5000 python-cicd-demo'
                }
            }
        }
    }
}

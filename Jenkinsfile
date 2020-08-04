def image = 'docker-registry.example.com/zap-scripts:latest'

pipeline {

    agent {
        label 'docker'
    }

    stages {
        stage('Start image') {
            steps {
                sh """
                    docker pull ${image}
                    docker run --rm ${image}
                """
            }
        }
    }
}

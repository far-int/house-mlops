pipeline {
  agent any

  stages {
    stage('Install dependencies') {
      steps {
        sh 'python3 --version'
        sh 'python3 -m pip install --upgrade pip --break-system-packages'
        sh 'python3 -m pip install -r requirements.txt --break-system-packages'
      }
    }

    stage('Train model') {
      steps {
        sh 'python3 train.py'
      }
    }
  }
}

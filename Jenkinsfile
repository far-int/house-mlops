pipeline {
  agent any

  stages {
    stage('Install dependencies') {
      steps {
        sh 'python3 --version'
        sh 'python3 -m pip install --upgrade pip'
        sh 'python3 -m pip install -r requirements.txt'
      }
    }

    stage('Train model') {
      steps {
        sh 'python3 train.py'
      }
    }
  }
}

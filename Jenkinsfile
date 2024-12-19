pipeline {
  agent any
  stages {
    stage('CHECKOUT CODE') {
      steps {
        git(url: 'https://github.com/OLUWAnelo/AUTOSMART-PROJECT', branch: 'master')
      }
    }

    stage('LOG') {
      steps {
        sh 'ls -la'
      }
    }

  }
}
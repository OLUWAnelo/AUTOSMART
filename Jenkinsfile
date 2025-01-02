pipeline {
  agent any
  stages {
    stage('CheckOut') {
      steps {
        git(url: 'https://github.com/OLUWAnelo/AUTOSMART-PROJECT', branch: 'master')
      }
    }

    stage('Log') {
      parallel {
        stage('Log') {
          steps {
            sh 'ls -la'
          }
        }

        stage('Runtest') {
          steps {
            sh 'pytest'
          }
        }

      }
    }

  }
}
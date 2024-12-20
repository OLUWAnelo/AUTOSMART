pipeline {
  agent any
  stages {
    stage('CHECKOUT CODE') {
      steps {
        git(url: 'https://github.com/OLUWAnelo/AUTOSMART-PROJECT', branch: 'master')
      }
    }

    stage('LOG') {
      parallel {
        stage('LOG') {
          steps {
            sh 'ls -la'
          }
        }

        stage('front-end unit test') {
          steps {
            sh ' cd autosmart-front && npm i && npm run test:unit'
          }
        }

      }
    }

  }
}
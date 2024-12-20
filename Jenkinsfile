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

        stage('Front-End Unit Test/Shell Script') {
          steps {
            sh ' cd autosmart-project-front && npm i && npm run test:unit'
          }
        }

        stage('Front-End Unit Tests/Shell Script') {
          steps {
            sh 'cd autosmart-project-front && npm i && npm run test:unit'
          }
        }

      }
    }

  }
}
pipeline {
  agent any
  stages {
    stage('gitlab') {
      steps {
        sh 'git@github.com:zerolugithub/pythonstudy.git'
      }
    }
    stage('OK') {
      steps {
        echo 'this is ok'
      }
    }
  }
}
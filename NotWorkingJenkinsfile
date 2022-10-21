pipeline {
    agent {
        docker {
            image 'python:3.9.12-alpine'
        }
    }
    environment {
        HOME = "${env.WORKSPACE}@tmp"
        BIN_PATH = "${HOME}/.local/bin/"
    }
    stages {
        stage('Git Clone') {
            steps {
                git changelog: false,  credentialsId: 'gitlabup', branch: 'bookless', url: "https://gitlab.com/chechkysh/hotelparadise.git"
            }
        }
        stage('Prepare') {
            steps {
                sh 'apk add postgresql-dev gcc python3-dev musl-dev'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
                sh 'pip install flake8'
                sh 'pip install mypy'
            }
        }
        stage('Test') {
            steps{
                sh 'python HotelDjango/manage.py makemigrations'
                sh 'python HotelDjango/manage.py test paradise'
                sh 'flake8 HotelDjango'
                sh 'mypy HotelDjango'
            }
        }
    }
}
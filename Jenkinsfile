pipeline {
  environment {
      DOCKER_USERNAME = credentials('docker-username')
      DOCKER_PASSWORD = credentials('docker-password')
  }
  agent {
    kubernetes {
      yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: python
    image: python
    command:
    - cat
    tty: true
  - name: docker
    image: docker:18.05-dind
    tty: true
    securityContext:
      privileged: true
    volumeMounts:
      - name: dind-storage
        mountPath: /var/lib/docker
  volumes:
  - name: dind-storage
    emptyDir: {}

"""
    }
  }
  stages {
    stage('Build and Test') {  
      steps {
        git url: 'http://kubernetes.docker.internal:30300/adybuxton/python-microservice.git'
        container('python'){
            sh """
               pip install -r requirements.txt
               pytest
               """
        }
        container('docker'){
            sh """
               docker build -f Dockerfile -t adybfjcns/python-microservice . --rm
               docker login -u $DOCKER_USERNAME -p '${DOCKER_PASSWORD}'
               docker push adybfjcns/python-microservice
               """
        }
      }
    }
  }
}
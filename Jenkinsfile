pipeline {
agent any
triggers {
// Poll GitHub every 2 minutes
pollSCM('H/2 * * * *')
}
stages {
stage('Checkout') {
steps {
git branch: 'main', url: 'https://github.com/MZG15/EECE430-movies-app.git'
}
}
stage('Build in Minikube Docker') {
steps {
bat '''
REM === Switch Docker to Minikube Docker ===
call minikube docker-env --shell=cmd > docker_env.bat
call docker_env.bat

# create docker image
    # cmds to get yaml file running docker
    # install docker for desktop (windows)
    # install docker compose (already built into docker desktop)
    # build process
        # docker-compose build python
    # starting the app
        # docker-compose up python
    # checking app works at defined port
        # go to localhost:5000
    # signing into docker hub online
        # docker login -u "username" -p "password" docker.io
    # push docker image to docker hub
        # docker-compose push python
# create rg-> az group create --name myAKSResourceGroup --location eastus
# create acr -> az acr create --resource-group myAKSResourceGroup --name pykub --sku Basic
# login to acr -> az acr login --name pykub
# retag local image for azure -> docker tag <localcontainer:image> <containername.azurecr.io>/obiwankubernetes/pyazure
# create aks cluster -> az aks create --resource-group myAKSResourceGroup --name myAKSCluster --node-count 1 --generate-ssh-keys
# get credentials of az aks get-credentials --resource-group myAKSResourceGroup --name myAKSCluster
# check if it is running -> kubectl get nodes
# prepare yaml manifest to deploy to aks
# deploy yaml manifest -> kubectl apply -f <yaml-file-name>
# get public facing url to test deployment and see app -> kubectl get service <appname> --watch
# go to url

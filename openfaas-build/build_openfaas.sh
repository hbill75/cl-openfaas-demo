#!/bin/zsh

# Output coloring
GREEN='\033[1;32m'
NC='\033[0m' # No Color

# Create openfaas namespaces (openfaas & openfaas-fn)
echo -e "\e[32mCreate OpenFaas namespaces...\e[0m\n" 
kubectl apply -f https://raw.githubusercontent.com/openfaas/faas-netes/master/namespaces.yml &&
sleep 5

# create openfaas uthentication credentials stored as a k8s secret
echo " "
echo -e "\e[32mCreate OpenFaas Password...\e[0m\n"
kubectl -n openfaas create secret generic basic-auth \
--from-literal=basic-auth-user=admin \
--from-literal=basic-auth-password=C1sco12345 &&
sleep 5
FAAS_USERNAME=$(kubectl -n openfaas get secret basic-auth -o jsonpath="{.data.basic-auth-user}" | base64 --decode)
FAAS_PASSWORD=$(kubectl -n openfaas get secret basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode)

# Display openfaas username & password
echo " "
echo -e "\e[32mDisplay OpenFaaS Username & Password\e[0m\n"
echo "OpenFaaS Username: $FAAS_USERNAME"
echo "OpenFaaS Password: $FAAS_PASSWORD"
sleep 5

# add the openfaas helm repository
echo " "
echo -e "\e[32mAdd the OpenFaas Helm Repository...\e[0m\n"
helm repo add openfaas https://openfaas.github.io/faas-netes/ &&
sleep 5

# Install openfaas using helm chart
echo " "
echo -e "\e[32mDeploy OpenFaas Services...\e[0m\n"
helm repo update && \
  helm upgrade openfaas --install openfaas/openfaas \
    --namespace openfaas  \
    --set functionNamespace=openfaas-fn \
    --set basic-auth=true &&
sleep 5

# Display openfaas UI and API gateway nodeport
echo " "
echo -e "\e[32mCheck Gateway Port...\e[0m\n"
kubectl get svc -n openfaas gateway-external -o wide &&
sleep 5
export OPENFAAS_URL=http://127.0.0.1:31112 &&

# Wait for openfaas services to start
echo " "
echo -e "\e[32mWaiting for OpenFaas Services to start...\e[0m"
sleep 6
echo -e "\e[32mWaiting for OpenFaas Services to start...\e[0m"
sleep 6
echo -e "\e[32mWaiting for OpenFaas Services to start...\e[0m"
sleep 6
echo -e "\e[32mWaiting for OpenFaas Services to start...\e[0m\n"
sleep 6

# Display status of openfaas services
kubectl -n openfaas get deployments -l "release=openfaas, app=openfaas"

# OpenFaaS CLI login
echo " "
echo -e "\e[32mLogin to OpenFaaS...\e[0m\n"
echo -n $FAAS_PASSWORD | faas-cli login --password-stdin
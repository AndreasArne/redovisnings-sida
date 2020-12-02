az network vnet create -g BTH-kmom01-aar-e20886 -n aarKubeVNet --address-prefix 173.0.0.0/16 --subnet-name aarSubnet --subnet-prefix 173.0.0.0/24


az vm create -n aar-kube-master -g BTH-kmom01-aar-e20886 --image Debian --size Standard_B2s --storage-sku Standard_LRS --os-disk-size-gb 30 --ssh-key-value /c/Users/aar/.ssh/id_rsa.pub --public-ip-address-dns-name aar-kubeadm-master


az vm create -n aar-kube-worker-1 -g BTH-kmom01-aar-e20886 --image Debian --size Standard_B1s --storage-sku Standard_LRS --os-disk-size-gb 30 --ssh-key-value /c/Users/aar/.ssh/id_rsa.pub --public-ip-address-dns-name aar-kubeadm-worker-1



# på alla
scp install.sh aar@aar-kubeadm-master.northeurope.cloudapp.azure.com: && ssh aar@aar-kubeadm-master.northeurope.cloudapp.azure.com
sudo apt update
sudo apt install gnupg software-properties-common docker.io rsync -y
sudo systemctl enable docker
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
sudo apt update
sudo apt install kubeadm -y


# master
sudo kubeadm init

# spara för att joina sen
# kör med sudo
kubeadm join 173.0.0.4:6443 --token nkg29v.ult91hsldi55wq00 \
    --discovery-token-ca-cert-hash sha256:06e8799522e4fb35fcfd23a962e37512eae0f0e6ebba63a5e6c5b7730dba017e

# master
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"


# kör sparade join

# kör lokalt
rsync -av microblog/kmom06 moc@13.69.184.156:/home/moc/


kubectl apply -f mysql-secrets.yml
kubectl apply -f mysql-pv.yml
kubectl apply -f mysql-deployment.yml
kubectl run -it --rm --image=mysql:5.7 --restart=Never mysql-client -- mysql -h mysql -ppass

kubectl apply -f microblog-deployment.yml

helm install nginx stable/nginx-ingress --set rbac.create=true
kubectl get svc

kubectl apply --validate=false -f https://raw.githubusercontent.com/jetstack/cert-manager/release-0.12/deploy/manifests/00-crds.yaml

kubectl create namespace cert-manager

helm repo add jetstack https://charts.jetstack.io

helm repo update

helm install cert-manager --namespace cert-manager --version v0.12.0

kubectl get pods --namespace cert-manager -w

kubectl apply -f issuer-staging.yml
kubectl apply -f issuer-prod.yml


kubectl apply -f ingress.yml
minikube start --driver=virtualbox
    möjliga fel:
        bcdedit /set hypervisorlaunchtype off i powershell
        gå in i settings och stäng av hyper-v
        minikube delete och gör om ovanstående

minikube addons enable ingress

kan testa minikube dashboard

minikube dashboard

stäng ner igen
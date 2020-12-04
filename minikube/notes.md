# skickar vidare request till docker daemon för minikube hittar inte den.
sudo socat UNIX-LISTEN:/var/run/docker.sock,user=<your_user_name>,fork TCP:127.0.0.1:2375

Kör windows istället.
https://minikube.sigs.k8s.io/docs/start/
testa kör echoservern

kubectl kommer med docker
kan köra `kubectl.exe get po` från wsl
och `minikube.exe`

tipsa om alias k='kubectl.exe'
alias m='minikube.exe'


https://www.studytrails.com/devops/kubernetes/install-minikube-and-docker-with-virtualbox-on-windows-10-home/
https://medium.com/better-programming/how-ingress-works-in-kubernetes-and-how-to-set-it-up-in-minikube-bb23d9086b1c

kan inte lägga till ingress addon om kör mot docker. behöver VM

bcdedit /set hypervisorlaunchtype off i powershell
gå in i settings och stäng av hyper-v
minikube start --driver=virtualbox

om kubectl redan installera kan man använda det.
Annars köra
minikube kubectl -- get po -A

kubectl kommando efter `--`.
Kan lägga till alias för kinikube kubectl --


efter kört 2. kör 2.5 för testa. Kör ` minikube service --url test-app -n minikube-example` för få ip och port att visa i webbläsaren.
Ta sen bort den igen ` kubectl delete -n minikube-example -f .\2.5-test-deploy.yml`

Behöver inte göra något för refresh av hosts file.
FUNKAR




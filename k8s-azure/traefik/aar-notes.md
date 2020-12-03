Jag kan få upp traefiks dashboard gui genom att köra filerna 1.-5. med `kubectl create -f <file>`

Sen kan man köra `kubectl describe svc traefik-ingress-service --namespace=kube-system` för att få fram porten till ui. Porten som är kopplad till dashboard:8100. För mig var det port 30768.

Sen kan jag gå till masternodens publicadns namn och den porten på slutet.

http://aar-kubeadm-master.northeurope.cloudapp.azure.com:30768


Sen blir det problem när jag försöker göra en mer dynamisk koppling till ui:t

Genom att köra 6.-7. filerna. Det får jag inte att fungera

Vilket är typ fram till och med steg 5 i https://medium.com/kubernetes-tutorials/deploying-traefik-as-ingress-controller-for-your-kubernetes-cluster-b03a0672ae0c
Då har jag också tagit hjälp av denna https://ralph.blog.imixs.com/2020/02/01/kubernetes-setup-traefik-2-1/
Såg nu också att samma blog hade en lite uppdaterad version https://ralph.blog.imixs.com/2020/04/05/traefik-v2-2-and-kubernetes-ingress/.


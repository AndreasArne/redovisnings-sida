Skapa och konfigurera servrar
======================

### 1scripts
Första steget i att gå mot automatisering. Mappen innehåller bash skript för att konfigurera en server och minska manuellt arbete.
Man behöver manuellt skapa en server på valfri molntjänst, kopiera över filerna och sen exekvera dem i ordning.
1-3 setup server, körs när server skapas som root
4-5 installera program, körs när server skapas som ny användare
6 setup databas, körs när server skapas som ny användare

#### Tankar

Packer för skripts 1-3, Terraform för att skapa servrar och installera packer image och Kubernetes för att orkestrera docker containrar på servrarna.
Skrips 4 är docker image.


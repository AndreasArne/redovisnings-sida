Skapa och konfigurera servrar
======================

### scripts

För alla skript behöver du först gå igenom dem och ersätta alla <...> med relevant data. T.ex. <password> ska ersättas med ett lösenord och <domain> ska ersättas av domännamnet du ska använda för din webbsida. Du behöver även göra detta för filerna i `resources/`! **Ersätt inte lösenorden lokalt och pusha till git!!!** Byt ut dem när du filerna på servern.

**10-first-minutes** innehåller skript för att sätta upp ny skapad server men ny användare m.m.

**deploy-app** innehåller skript för att sätta upp och starta appen med nginx och allt.



#### Tankar

Packer för skripts 1-3, Terraform för att skapa servrar och installera packer image och Kubernetes för att orkestrera docker containrar på servrarna.
Skrips 4 är docker image.



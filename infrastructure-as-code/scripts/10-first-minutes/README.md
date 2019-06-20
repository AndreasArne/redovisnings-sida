
Första 10 minuter på en server, som skript
==========================================

Mappen innehåller skript som gör utför det mesta från https://dbwebb.se/kunskap/github-education-pack-och-en-server-pa-digital-ocean#first10, så man slipper göra det manuellt.

Att notera, skripten utgår ifrån att du har lagt in din ssh nyckel på Digital Ocean och skapar servern med dem. Den kopieras från root användaren till användaren som skapas i skripten.

Gå igenom skripten och ersätt alla `<...>` med passande innehåll.



# Utförande

1. Skapa en DO droplet, glöm inte att klicka i din ssh nyckel.

2. Kopiera över mappen med skripten till din droplet.
    - `scp -r 10-first-minutes root@<droplet-ip>:`

3. Logga in på servern med ssh.
    - `ssh root@<ip>`

4. Exekvera skripten i ordning.

5 Profit!

Nu är du redo att göra något med din server. Stäng ner din ssh koppling och logga in igen med användaren `deploy` istället för root.

Om du är uppmärksam så är inte allt från artikeln med i skripten. Om du vill ha med resterande kan du lägga till fler skript själv eller göra det manuellt.

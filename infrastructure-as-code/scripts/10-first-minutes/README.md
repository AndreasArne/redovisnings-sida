
Första 10 minuter på en server, som skript
==========================================

Mappen innehåller skript som gör utför det mesta från https://dbwebb.se/kunskap/github-education-pack-och-en-server-pa-digital-ocean#first10, så man slipper göra det manuellt.

Att notera, skripten utgår ifrån att du har lagt in din ssh nyckel på AWS och skapar servern med dem. Den kopieras från original användaren till användaren som skapas i skripten.

I vissa av skripten skapas det variabler överst i filerna, ersätt värdena i dem till något passande, ex. `<password>` ska ersättas med ett lösenord.



# Utförande

1. Skapa en virtuell server, glöm inte att klicka i din ssh nyckel.

2. Kopiera över mappen med skripten till din server.
    - `scp -r 10-first-minutes <user>@<ip>:`

3. Logga in på servern med ssh.
    - `ssh <user>@<ip>`

4. Byt till root användaren, `sudo su`.

5. Exekvera skripten i ordning.

6. Logga ut från servern och logga in igen med `deploy` användaren för att raden original användaren, `userdel -r ubuntu`.

7.  Profit!

8. Om du vill ha lite mer säkerhet kan du ta bort root lösenordet, använd kommandot `passwd -d root`.

Nu är du redo att göra något med din server. Stäng ner din ssh koppling och logga in igen med användaren `deploy` istället för root.

Om du är uppmärksam så är inte allt från artikeln med i skripten. Om du vill ha med resterande kan du lägga till fler skript själv eller göra det manuellt.

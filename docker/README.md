Build image:

```
docker build -t microblog:latest -f docker/Dockerfile .
```

Start container:

```
docker run --name microblog -d -p 8000:5000 --rm -e SECRET_KEY=my-secret-key \
    -e DATABASE_URL=mysql+pymysql://microblog:database-password@dbserver/microblog \
    --link mysql:dbserver \
    microblog:latest
```

Start mysql container:

```
docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_USER=microblog \
    -e MYSQL_DATABASE=microblog \
    -e MYSQL_PASSWORD=database-password \
    mysql/mysql-server:5.7
```

composer docu: https://docs.docker.com/compose/compose-file/
Good blog about docker: https://vsupalov.com/database-in-docker/
Config for mysql docker: https://webapplicationconsultant.com/docker/how-to-override-mysql-config-in-docker/
Backup mysql data from container: https://webapplicationconsultant.com/docker/what-is-the-best-way-to-setup-latest-wordpress-blog-using-docker/
docker for dev and production: https://vsupalov.com/same-dockerfile-dev-staging-production/ https://medium.com/vteam/configure-docker-project-for-different-environments-using-docker-compose-3-bfbef37d951c


Docker on CircleCi:
https://circleci.com/blog/docker-what-you-should-know/
https://circleci.com/blog/adding-application-and-image-scanning-to-your-cicd-pipeline/

### Errors

In WSL:
```
docker.errors.DockerException: Credentials store error: StoreError('docker-credential-docker-credential-desktop.exe not installed or not available in PATH',)
```
Open `~/.docker/config.json` and add `.exe` to the `credsStore`. 
```
"credsStore":"desktop.exe"
```

Installing python modules in docker slim/alpine:
```
unable to execute 'gcc': No such file or directory
    error: command 'gcc' failed with exit status 1
```
Install `gcc`:
```
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && apk del build-dependencies
```
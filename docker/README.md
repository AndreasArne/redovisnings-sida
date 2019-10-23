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


Good blog about docker: https://vsupalov.com/database-in-docker/

composer docu: https://docs.docker.com/compose/compose-file/
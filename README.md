## Quickstart

1. You must first define some env variables. For convenience you can just source `envrc`.
   You can edit the file if you want but for the tests it should be fine to keep the defaults:

``` bash
source envrc
```

2. Start the Postgresql database:

``` bash
docker-compose up -d
```

3. Try connecting to the database:

``` bash
pgcli -U $USER -h $HOST -p $PORT $DB
```

If you defined `$PASS` on `envrc` then you might need to call `pgcli` with `-W` so that it will
prompt you for a password.

4. If you can connect, you are ready to start using SQLAlchemy and Alebmic!

## Reset database

Running the following commands should get rid of the database instance and its data

``` bash
docker-compose rm --stop --force
docker volume rm sqlalchemyplayground_pg-data
```

If you also want to remove the existing migrations, you can do it with:

``` bash
rm -rf migrations/versions/*
```

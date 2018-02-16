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
pgcli -U $PG_USER -W $PG_PASS -h $PG_HOST -p $PG_PORT $PG_DB
```

4. If you can connect, you are ready to start using SQLAlchemy and Alebmic!


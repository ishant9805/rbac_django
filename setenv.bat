@echo off
cd slate_root
set PGUSER=POSTGRESQL_USER
set PGPORT=POSTGRESQL_PORT
set PGHOST=POSTGRESQL_HOST
set PGPASS=YOURPGPASS
set PGDATABASE=DATABASE_NAME
echo Environment has been set.
echo Starting server...
py manage.py runserver
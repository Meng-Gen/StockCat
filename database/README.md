Database
--------

To store analysis data we select PostgreSQL as our database.


Management Tool
---------------
[pgAdmin3](http://www.pgadmin.org/)

PostgreSQL Interactive Terminal (```psql```)
-------------------------------
* Login as admin: ```psql --username=postgres```
* List databases: ```\list```
* Connect database: ```\connect <database_name>```
* List tables: ```\d``` or ```\d+```
* Show table schema: ```\d <table_name>``` or ```\d+ <table_name>```
* Query: ```<sql_query>;``` *DON'T forget semicolon (;)*

Setup Development Environment
-----------------------------
1. Login as admin: ```psql --username=postgres```
2. Create role: ```CREATE ROLE stockcat;``` (Might check by ```SELECT rolname FROM pg_roles;```)
3. Create database: ```CREATE DATABASE stockcat OWNER stockcat;``` 

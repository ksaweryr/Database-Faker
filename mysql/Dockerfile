FROM mysql:latest

COPY schema.sql /docker-entrypoint-initdb.d
HEALTHCHECK --interval=2s --retries=10 CMD mysqladmin ping --silent

EXPOSE 3306
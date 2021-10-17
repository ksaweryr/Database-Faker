FROM postgres:alpine

COPY schema.sql /docker-entrypoint-initdb.d
HEALTHCHECK --interval=2s --retries=10 CMD pg_isready -q

EXPOSE 5432
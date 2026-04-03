# AIRA Data Platform Challenge 1

## Setup

docker-compose up -d

alembic upgrade head

uvicorn main:app --reload

## Features

- Multi-tenant schema
- PostgreSQL RLS
- Batch event ingestion
- Bulk inserts
- Partition-ready event table
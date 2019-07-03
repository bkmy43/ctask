#!/usr/bin/env bash

PGUSER=postgres PGPASSWORD=docker psql -h localhost postgres -f init_database.sql
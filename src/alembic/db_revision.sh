#!/bin/bash

# db_revision.sh
set -e  # Exit on any error

# Set PYTHONPATH to current directory
export PYTHONPATH=$(pwd)

# Check if migration message is provided
if [ -z "$1" ]; then
    echo "Error: Please provide a migration message"
    echo "Usage: ./db_revision.sh 'your migration message'"
    exit 1
fi

# Turn on auto-export
set -a
# Load environment variables from .env
if [ -f "../.env" ]; then
    source ../.env
else
    echo "Error: .env file not found in parent directory"
    exit 1
fi
# Turn off auto-export
set +a

# For Alembic, use psycopg2 (sync driver) instead of asyncpg
export DB_URL="postgresql+psycopg2://${DB_USER}:${DB_PASS}@127.0.0.1:${DB_EXTERNAL_PORT}/${DB_NAME}"

echo "Using DB_URL: $DB_URL"
echo "Creating migration: $1"

# Generate migration
alembic revision --autogenerate -m "$1"

echo "Migration created successfully!"
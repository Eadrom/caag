#!/usr/bin/env python

# Development SQLite URL
DATABASE_URL_DEV = "sqlite:///./test.db"

# Production PostgreSQL URL
DATABASE_URL_PROD = "postgresql://username:password@localhost:5432/production_db"

# Secret key for FastAPI app
SECRET_KEY = "mysecretkey"

# Enable or disable debug mode
DEBUG = True

# Logging level
LOG_LEVEL = "INFO"

# Remote feeds
REMOTE_FEEDS = {
    "remote_url_1": "your_api_key_1",
    "remote_url_2": "your_api_key_2",
}

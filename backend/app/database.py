from pymongo import MongoClient
from pymongo.database import Database

from app.config import MONGODB_DATABASE, MONGODB_URL

_client: MongoClient | None = None
_database: Database | None = None


def connect_to_mongo() -> None:
    global _client, _database

    client = MongoClient(MONGODB_URL, serverSelectionTimeoutMS=5000)
    try:
        client.admin.command("ping")
    except Exception:
        client.close()
        raise

    _client = client
    _database = client[MONGODB_DATABASE]


def close_mongo_connection() -> None:
    global _client, _database

    if _client is not None:
        _client.close()
    _client = None
    _database = None


def get_database() -> Database:
    if _database is None:
        raise RuntimeError("MongoDB connection has not been initialized")
    return _database
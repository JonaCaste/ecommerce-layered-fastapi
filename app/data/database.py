"""
Database connection module.

This module establishes a connection pool to a MySQL database using credentials
stored in a .env file. The connection is reused across services for querying and
executing SQL statements.
"""

import os
import mysql.connector
from mysql.connector import pooling
from dotenv import load_dotenv

load_dotenv()

dbconfig = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

# Create a connection pool with a maximum of 5 simultaneous connections
connection_pool = pooling.MySQLConnectionPool(pool_name="mypool",
                                              pool_size=5,
                                              **dbconfig)


def get_connection():
    """
    Retrieve a connection from the pool.

    Returns:
        MySQLConnection: An active database connection.
    """
    return connection_pool.get_connection()

#!/usr/bin/env python3
"""
MySQL Database Creation Script for ALX Book Store
Creates the alx_book_store database if it doesn't exist
"""

try:
    import pymysql
    pymysql.install_as_MySQLdb()
    import MySQLdb
    USING_PYMYSQL = True
except ImportError:
    try:
        import mysql.connector
        USING_PYMYSQL = False
    except ImportError:
        print("Error: No MySQL connector found. Please install either:")
        print("  pip install pymysql")
        print("  OR")
        print("  pip install mysql-connector-python")
        exit(1)

def create_database():
    """Create the alx_book_store database"""
    connection = None
    try:
        # Connect to MySQL server without specifying a database
        if USING_PYMYSQL:
            connection = MySQLdb.connect(
                host='localhost',
                user='root',      
                password='VenomSnakeMGS5',      
                charset='utf8mb4'
            )
        else:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',      
                password='VenomSnakeMGS5'       
            )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to connect to the database server")
        print("Please check your MySQL credentials and ensure MySQL server is running")
        
    finally:
        # Close connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed")

if __name__ == "__main__":
    create_database()
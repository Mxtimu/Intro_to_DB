#!/usr/bin/env python3
"""
MySQL Database Creation Script for ALX Book Store using PyMySQL
"""

import pymysql
from pymysql import Error

def create_database():
    """Create the alx_book_store database"""
    connection = None
    try:
       
        connection = pymysql.connect(
            host='localhost',
            user='root',      
            password='VenomSnakeMGS5',      
            charset='utf8mb4'
        )
        
        with connection.cursor() as cursor:
           
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
        connection.commit()
        print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error: {e}")
        print("Failed to connect to the database server")
        
    finally:
      
        if connection:
            connection.close()
            print("Database connection closed")

if __name__ == "__main__":
    create_database()
import mysql.connector
from mysql.connector import Error
import configparser

def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().split(';')

def create_database_and_tables(sql_commands, db_config):
    try:
        # Connect to MySQL Server
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Execute each SQL command
        for command in sql_commands:
            if command.strip():
                cursor.execute(command)

        print("Database and tables created successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    # Read database configuration from config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')

    db_config = {
        'host': config['mysql']['host'],
        'user': config['mysql']['user'],
        'passwd': config['mysql']['password']
    }

    # Initialize conn as None
    conn = None

    try:
        # Read SQL commands from database_setup.sql
        sql_commands = read_sql_file('database_setup.sql')

        # Create database and tables
        create_database_and_tables(sql_commands, db_config)
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
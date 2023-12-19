import mysql.connector
from mysql.connector import Error
import configparser

def check_tables_in_database(db_config):
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Show tables
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        print("Tables in the database:")
        for table in tables:
            print(table[0])  # Table name is in the first column

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    # Read database configuration from config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')

    db_config = {
        'host': config['mysql']['host'],
        'user': config['mysql']['user'],
        'passwd': config['mysql']['password'],
        'database': config['mysql']['database']
    }

    # Check tables in the database
    check_tables_in_database(db_config)

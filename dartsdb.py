import mysql.connector

conn_params = { 'database' : 'dartsdb',
                'host' : 'localhost',
                'user' : 'angus',
                'password' : 'thommo25'}

def connect():

    return mysql.connector.connect(**conn_params)

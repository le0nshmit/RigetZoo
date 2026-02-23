import sqlite3

def initiliase_database():
    connection = sqlite3.connect('app/data/data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS data(forename, surname, dob, password)')


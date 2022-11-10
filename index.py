import sqlite3
import serial 

porta="COM8"
baudeRate=9600
umidade=0

connection = sqlite3.connect('banco-de-dados.db')

with open('./schema.sql') as f:
  connection.executescript(f.read())

cursor = connection.cursor()

def add_to_database(cursor, value):
  cursor.execute('INSERT INTO umidades (value) VALUES (?);', [value])

add_to_database(cursor, '123')
add_to_database(cursor, '321')
add_to_database(cursor, '32903213')

import sqlite3


conexão = sqlite3.connect('carros.db')
cursor = conexão.cursor()

cursor.execute('Selecione * de carros')
registros = cursor.fetchall()
conexão.close()

print(registros)
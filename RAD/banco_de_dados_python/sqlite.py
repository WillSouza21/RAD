import sqlite3
banco = sqlite3.connect('database.db')

#para escrever em sql, para inserir os dados, deletar, as manipulações no banco
cursor = banco.cursor()

#criar tabela para o banco, se ja criou a tabela comenta
cursor.execute("CREATE TABLE cliente(nome text, idade integer, sex text)")

#inserir dados

cursor.execute("INSERT INTO cliente VALUES('Cynthia', 40, 'f'), ('pedro', 20, 'm')")
banco.commit()
#inserir novo registro
cursor.execute("INSERT INTO cliente  VALUES('carla', 20, 'f'),('tiago', 30, 'm')")
#confirmando que esta inserindo no banco
banco.commit()

cursor.execute("Select * from cliente")
print(cursor.fetchall())

#fechamos o cursor e a conexão, respectivamente.
cursor.close()
banco.close()
'''import os
os.remove('database.db')'''
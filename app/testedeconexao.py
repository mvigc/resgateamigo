import mysql.connector as mysql

try:
    conexao = mysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='',
        database='banco' 
    )

    print('Conectado com sucesso!')
except Exception as err:
    print('Houve um erro ao conectar')
    print(err)
import mysql.connector as mysql

try:
    conexao = mysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='',
        database='banco' 
    )

    cursor = conexao.cursor()

    # Exemplo de inserção de uma nova pessoa
    id = '123'
    nome = 'bella'
    sexo = 'femea'
    pelagem = 'branca'
    data_nascimento = '22/03/2004'
    castracao = 'sim'
    saude = 'vacina v5'
    

    # Query SQL para inserir uma nova pessoa
    query_inserir_gato = "INSERT INTO gato (id, nome, sexo, pelagem, data_nascimento, castracao, saude) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    
    # Dados para inserção
    dados_gato = (id, nome, sexo, pelagem, data_nascimento, castracao, saude)

    # Executar a query
    cursor.execute(query_inserir_gato, dados_gato)

    # Confirmar a operação
    conexao.commit()

    print('Gato inserido com sucesso!')
except Exception as err:
    print('Houve um erro ao inserir gato')
    print(err)
finally:
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print('Conexão encerrada.')
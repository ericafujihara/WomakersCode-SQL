"""
Este é um script para demonstrar uma conexão básica com um banco de dados SQLite e alguns comandos como:
- Criação de tabelas
- Update de informações em tabelas existentes
- Exclusão de registros em tabelas
- Seleção de informações que atendem à uma determinada condição
- Junção de tabelas

"""

import sqlite3

conexao = sqlite3.connect('bancodedados')  
cursor = conexao.cursor()  

#Criar uma tabela chamada "alunos" com campos: id, nome, idade e curso
cursor.execute('CREATE TABLE  alunos(id INT, nome VARCHAR(200), idade INT, curso VARCHAR(200))')

cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Erica", "35", "Data Analytics")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Mônica", "29", "Psicologia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Edward", "34", "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Felipe", "20", "Publicidade e Propaganda")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Ellen", "42", "Design")')

# # --------------------- Consultas básicas --------------------- 
# #Selecionar todos os registros da tabela alunos
dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
    print(aluno)
print("----------------------------------------------------------------------")

# #Selecionar o nome e a idade dos alunos com mais de 20 anos
dados = cursor.execute('SELECT nome, idade FROM alunos where idade>20')
for aluno in dados:
    print(aluno)

# print("----------------------------------------------------------------------")
# #Selecionar os alunos do curso de "Engenharia" em ordem alfabética

dados = cursor.execute('SELECT nome FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
for aluno in dados:
    print(aluno)
print("----------------------------------------------------------------------")


# # --------------------- Atualização e remoção  --------------------- 
# # Atualizar a idade de um aluno específico na tabela
cursor.execute('UPDATE alunos SET idade = 19 where nome = "Felipe" ')
dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
    print(aluno)
print("----------------------------------------------------------------------")


# # Remover um aluno pelo ID
cursor.execute('DELETE FROM alunos WHERE id = 4')
dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
    print(aluno)
print("----------------------------------------------------------------------")


# --------------------- CRIAR UMA TABELA E INSERIR DADOS  --------------------- 
# Criar uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

cursor.execute('CREATE TABLE  clientes(id INT, nome VARCHAR(200), idade INT, saldo FLOAT)')

cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Camila", "25", 123.58)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Thiessa", "29", 800.35)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Caio", "36", 1468.7)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Roseli", "40", 36.97)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Ricardo", "48", 305.46)')


# # --------------------- CONSULTAS E FUNÇÕES AGREGADAS  --------------------- 
# # Selecionar o nome e a idade dos clientes com idade superior a 30 anos.

cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
dados = cursor.execute('SELECT * FROM clientes')
for cliente in dados:
    print(cliente)
print("----------------------------------------------------------------------")

# # Calcular o saldo médio dos clientes
cursor.execute('SELECT avg(saldo) as saldo_medio FROM clientes ')
resultado = cursor.fetchone()

if resultado:
    saldo_medio = resultado[0]
    print(f"Saldo Médio dos Clientes: {saldo_medio}")
else:
    print("Não há dados disponíveis.")
print("----------------------------------------------------------------------")


# # Encontrar o cliente com saldo máximo
cursor.execute('SELECT nome, MAX(saldo) as saldo_max FROM clientes ')
resultado = cursor.fetchone()

if resultado:
    nome_cliente = resultado[0]
    saldo_max = resultado[1]
    print(f"O cliente com o maior saldo é: {nome_cliente}")
    print(f"Saldo: {saldo_max}")
else:
    print("Não há dados disponíveis.")

print("----------------------------------------------------------------------")

# # Contar quantos clientes têm saldo acima de 1000

cursor.execute('SELECT count(nome) as qdt_clientes FROM clientes where saldo > 1000 ')
resultado = cursor.fetchone()

if resultado:
    qtd_clientes = resultado[0]
    
    print(f"Há {qtd_clientes} cliente(s) com saldo maior que 1000")
    
else:
    print("Não há dados disponíveis.")

print("----------------------------------------------------------------------")


# # --------------------- ATUALIZAÇÃO E REMOÇÃO COM CONDIÇÕES  --------------------- 
#Atualizar o saldo de um cliente específico
cursor.execute('UPDATE clientes SET saldo = 0 where nome = "Caio" ')
dados = cursor.execute('SELECT * FROM clientes')
for cliente in dados:
    print(cliente)
print("----------------------------------------------------------------------")


# #Remover um cliente pelo seu ID

cursor.execute('DELETE FROM clientes WHERE id = 1')
dados = cursor.execute('SELECT * FROM clientes')
for cliente in dados:
    print(cliente)
print("----------------------------------------------------------------------")

# --------------------- JUNÇÃO DE TABELAS  --------------------- 
# Crie uma segunda tabela chamada "compras" com os campos: id(chave primária), cliente_id(chave estrangeira referenciando o id da tabela clientes), produto(texto) e valor(real). Insira algumas compras associadas a clientes existentes na tabela 'clientes'. Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra


cursor.execute('CREATE TABLE  compras(id INT, cliente_id INT, produto VARCHAR(100), valor FLOAT)')

cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1, 1, "Kit Brocas Bosh",99.70)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2, 1, "Tesoura para poda",22.90)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (3, 3,"Farinha sem glúten", 12.90)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (4, 2,"Robô Aspirador", 426.55)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (5, 2,"Vela aromática",85.90)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (3, 4,"Forma de gelo flexível",13.10)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (4, 4,"Chaleira elétrica",83.69)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (5, 5,"Ventilador de teto",259.80)')

#Exibir o nome do cliente, o produto e o valor de cada compra
dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor  FROM clientes LEFT JOIN compras on clientes.id = compras.cliente_id')
for cliente in dados:
    print(cliente)

#cursor.execute('DROP TABLE user')
conexao.commit()
conexao.close
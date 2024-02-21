# WomakersCode-SQL
 Este projeto em Python utiliza SQLite para criar e manipular um banco de dados simples com duas tabelas: "alunos" e "clientes". Abaixo, você encontrará um resumo das principais funcionalidades e instruções de uso.

1. Tabela "alunos"
Criação da Tabela:

    A tabela "alunos" é criada com os campos: id, nome, idade e curso.
    São inseridos registros na tabela "alunos" com informações fictícias.

Consultas que foram realizadas:

    a. Exibir todos os registros da tabela "alunos".
    b. Selecionar o nome e a idade dos alunos com mais de 20 anos.
    c. Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

Atualização e Remoção:

Atualiza a idade de um aluno específico na tabela.
Remove um aluno pelo id.
2. Tabela "clientes"
Criação da Tabela:

    A tabela "clientes" é criada com os campos: id, nome, idade e saldo.

    São inseridos registros na tabela "clientes" com informações fictícias.

Consultas e Funções Agregadoras:

Seleciona o nome e a idade dos clientes com idade superior a 30 anos.
Calcula o saldo médio dos clientes.
Encontra o cliente com o saldo máximo.
Conta quantos clientes têm saldo acima de 1000.
Atualização e Remoção com Condições:

Atualiza o saldo de um cliente específico.
Remove um cliente pelo seu id.
3. Junção de Tabelas "clientes" e "compras"
Criação da Tabela "compras":

A tabela "compras" é criada com os campos: id, cliente_id, produto e valor.
Inserção de Dados em "compras":

Junção de Tabelas:

    Exibe o nome do cliente, o produto e o valor de cada compra através de uma junção entre "clientes" e "compras".



Execução do Código:
    Para executar este código, certifique-se de ter o SQLite instalado e utilize um ambiente Python compatível. O código cria, popula e consulta um banco de dados SQLite localmente.

Sistema de Cadastro de Usuários - SQLite
Este é um programa em Python que utiliza um banco de dados SQLite para realizar operações de cadastro, leitura, atualização e exclusão de usuários.

Funções Principais:

• criar_tabela()
Cria a tabela usuarios no banco de dados se ela não existir.

• cadastrar_usuario(nome, idade)
Adiciona um novo usuário ao banco de dados.

• listar_usuarios()
Exibe todos os usuários cadastrados no banco de dados.

• atualizar_usuario(usuario_id, novo_nome, nova_idade)
Atualiza as informações de um usuário no banco de dados.

• excluir_usuario(usuario_id)
Remove um usuário do banco de dados.

Estrutura do Projeto:

O código utiliza a biblioteca sqlite3 para interagir com o banco de dados SQLite e realizar as operações de CRUD (Create, Read, Update, Delete).

Loop Principal
O programa entra em um loop que permite ao usuário escolher entre diferentes operações, como cadastrar, listar, atualizar, excluir usuários ou sair do programa.

Como Usar:

1. Clone o repositório:
  
git clone https://github.com/kyliews/Usuarios_SQL3

2.Navegue até o diretório do projeto:

cd Usuarios_SQL3

3. Execute o script Python:

python psql.py

Interaja com o banco de dados agora.

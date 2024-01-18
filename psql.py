import sqlite3
 
def criar_tabela():
    conexao = sqlite3.connect("cadastro.db")
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios ( 
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL)
                    ''')
    conexao.commit()
    conexao.close()
    
def cadastrar_usuario(nome, idade):
    conexao = sqlite3.connect("cadastro.db")
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', (nome, idade))
    conexao.commit()
    conexao.close()
    
def listar_usuarios():
    conexao = sqlite3.connect("cadastro.db")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Idade: {usuario[2]}")
    conexao.close()
    
def atualizar_usuario(usuario_id, novo_nome, nova_idade):
    conexao = sqlite3.connect("cadastro.db")
    cursor = conexao.cursor()
    cursor.execute('UPDATE usuarios SET nome=?, idade=? WHERE id=?', (novo_nome, nova_idade, usuario_id))
    conexao.commit()
    conexao.close()
    
def excluir_usuario(usuario_id):
    conexao = sqlite3.connect("cadastro.db")
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id=?', (usuario_id,))
    conexao.commit()
    conexao.close()
    
    
criar_tabela() 

while True:
    print("\nEscolha uma operação: ")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Excluir usuário")
    print("0 - Sair")
    
    escolha = input("Digite o número da operação desejada: ")
        
    if escolha == "1":
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        cadastrar_usuario(nome, idade)
        
    elif escolha =="2":
        listar_usuarios()
        
    elif escolha =="3":
        usuario_id = int(input("Digite o ID do usuário que deseja atualizar: "))
        novo_nome = input("Digite o novo nome: ")
        nova_idade = int(input("Digite a nova idade: "))
        atualizar_usuario(usuario_id, novo_nome, nova_idade)
        
    elif escolha =="4":
        usuario_id = input("Digite o ID do usuário que deseja excluir: ")
        excluir_usuario(usuario_id)
        
    elif escolha == "0":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
    

    

                    
                  
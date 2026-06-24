import sqlite3

def conectar():
    return sqlite3.connect("jogo.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS personagens (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   classe TEXT NOT NULL,
                   vida INTEGER NOT NULL,
                   ouro INTEGER NOT NULL)""")
    
    conexao.commit()
    conexao.close()

def listar_personagens():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                   SELECT * FROM personagens""")
    personagens = cursor.fetchall()

    if personagens:
        print("\n-- PERSONAGENS--")
        for personagem in personagens:
            print(f'ID: {personagem[0]}')
            print(f'Nome: {personagem[1]}')
            print(f'Classe: {personagem[2]}')
            print(f'Vida:  {personagem[3]}')
            print(f'Ouro: {personagem[4]}')
            print("--------------------------------- \n")

    else:
        print("Nenhum personagem encontrado")

    conexao.close()

def criar_personagem():
    nome = input("Nome do personagem: ")
    classe = input("Classe do personagem: ")
    vida = input("Vida do personagem: ")
    ouro = input("Ouro do personagem: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""INSERT INTO personagens (nome, classe, vida, ouro)
                   VALUES(?,?,?,?)""",
                   (nome,classe,vida,ouro))
    
    conexao.commit()
    conexao.close()

def mostrar_menu():
        print(""" ========== MENU DO JOGO ==========
1 - Listar personagens 
2 - Criar personagem 
0 - Sair 
=================================== """) 


def executar_programa():
    criar_tabela()
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            listar_personagens()
        elif opcao == "2":
            criar_personagem()
        elif opcao == "0":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida.")

executar_programa()
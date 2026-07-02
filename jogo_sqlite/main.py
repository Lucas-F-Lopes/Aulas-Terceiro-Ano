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

# Buscar personagem por ID
def buscar_personagem_por_id():
    id_personagem = int(input("Digite o ID do personagem: "))
    
    conexao = conectar ()
    cursor = conexao.cursor()

    cursor.execute("""  
    SELECT * FROM personagens 
    WHERE id = ?
    """, (id_personagem,))

    personagem = cursor.fetchone()

    if personagem: 
        print("\n-- PERSONAGEM ENCONTRADO --")
        print(f'ID: {personagem[0]}')
        print(f'Nome: {personagem[1]}')
        print(f'Classe: {personagem[2]}')
        print(f'Vida: {personagem[3]}')
        print(f'Ouro: {personagem[4]}')
        print("--------------------------------- \n")
    else:
        print("Personagem não encontrado.")
    
    conexao.close()

def ganhar_ouro():
    id_personagem = int(input("Digite o ID do personagem: "))
    quantidade_ouro = int(input("Digite a quantidade de ouro a ser adicionada: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                   UPDATE personagens
                   SET ouro = ouro + ?
                   WHERE id = ?""",
                   (quantidade_ouro, id_personagem))
    
    if cursor.rowcount > 0:
        print(f"{quantidade_ouro} de ouro adicionado ao personagem com ID {id_personagem}.")
    else:
        print("Personagem não encontrado.")

    conexao.commit()
    conexao.close()
    
def mostrar_menu():
        print("""\n ========== MENU DO JOGO ==========
1 - Listar personagens 
2 - Criar personagem 
3 - Buscar personagem por ID
4 - Ganhar ouro
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
        elif opcao == "3":
            buscar_personagem_por_id()
        elif opcao == "4":
            ganhar_ouro()
        elif opcao == "0":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida.")

executar_programa()
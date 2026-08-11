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
    vida = ler_numero_inteiro("Vida do personagem: ")
    ouro = ler_numero_inteiro("Ouro do personagem: ")

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
5 - Receber dano
6 - Mudar classe do personagem
7 - Deletar personagem
8 - Ranking de ouro
0 - Sair 
=================================== """) 

def receber_dano():
    id_personagem = int(input("ID do personagem: "))
    quantidade_dano = int(input("Quanto dano ele recebeu? "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT vida FROM personagens WHERE id = ?
    """, (id_personagem,))

    resultado = cursor.fetchone()

    if resultado:
        vida_atual = resultado[0]

        if vida_atual == 0:
            print("Esse personagem já está sem vida!")
        else:
            nova_vida = vida_atual - quantidade_dano

            if nova_vida < 0:
                nova_vida = 0

            cursor.execute("""
            UPDATE personagens
            SET vida = ?
            WHERE id = ?
            """, (nova_vida, id_personagem))

            conexao.commit()
            print(f"Dano aplicado! Vida atual: {nova_vida}")

    else:
        print("Personagem não encontrado.")

    conexao.close()

def mudar_classe_personagem():
    id_personagem = int(input("Digite o ID do personagem: "))
    nova_classe = input("Digite a nova classe do personagem: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                   UPDATE personagens
                   SET classe = ?
                   WHERE id = ?""",
                   (nova_classe, id_personagem))
    
    if cursor.rowcount > 0:
        print(f"Classe do personagem com ID {id_personagem} alterada para {nova_classe}.")
    else:
        print("Personagem não encontrado.")

    conexao.commit()
    conexao.close()

def deletar_personagem():
    id_personagem = int(input("Digite o ID do personagem a ser deletado: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                   DELETE FROM personagens
                   WHERE id = ?""",
                   (id_personagem,))
    
    if cursor.rowcount > 0:
        print(f"Personagem com ID {id_personagem} deletado com sucesso.")
    else:
        print("Personagem não encontrado.")

    conexao.commit()
    conexao.close()

def ranking_ouro():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                   SELECT nome, classe, ouro FROM personagens
                   ORDER BY ouro DESC
                   LIMIT 3""")
    
    ranking = cursor.fetchall()

    if ranking:
        print("\n--TOP 3 PERSONAGENS MAIS RICOS--")
        for posicao, personagem in enumerate(ranking, start=1):
            nome, classe, ouro = personagem
            print(f"{posicao}º - {nome} ({classe}): {ouro} de ouro")
    else:
        print("Nenhum personagem encontrado.")

    conexao.close()

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
        elif opcao == "5":
            receber_dano()
        elif opcao == "6":
            mudar_classe_personagem()
        elif opcao == "7":
            deletar_personagem()
        elif opcao == "8":
            ranking_ouro()
        elif opcao == "0":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida.")

def ler_numero_inteiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

executar_programa()
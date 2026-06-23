# 02
# Escreva um programa onde: 
# - Pergunte ao usuário o que ele gosta de jogar (seja esporte ou jogos online) 
# - Pergunte ao usuário como é a descrição do jogo, o que ele faz no jogo (pode ser uma experiência)
# - Devolva em tela: "Gosto de jogar {jogo}, para que vocês conheçam melhor o jogo irei falar um pouco dele {informacao}"

jogo = input("Qual jogo você gosta de jogar?\n ")
descricao = input("Fale algo sobre o jogo! Pode ser uma experiência: ")

print (f"Gosto de jogar {jogo}, para que vocês conheçam melhor o jogo irei falar um pouco dele:\n{descricao}")
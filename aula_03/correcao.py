class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e eu trabalho como {self.profissao}.")

mendigo = Pessoa("Renan", 67, "Mendigo")
mendigo.apresentar()
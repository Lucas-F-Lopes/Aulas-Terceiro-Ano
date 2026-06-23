# Primeira Classes
# Conceitos: class, __ini__, self, atributos, métodos

class Animal:
    """Representa um animal genérico"""

    def __init__(self, nome, especie, som):
        # atributos de instância - cada objeto terá o seu
        self.nome = nome
        self.especie = especie
        self.som = som
        self.energia = 100 # Todos começam com a energia cheia

    def falar(self):
        print(f"{self.nome} diz: {self.som}!")

    def comer(self):
        self.energia += 20
        print(f"{self.nome} comeu. Energia: {self.energia}")

    def status(self):
        print(f"\n--- {self.nome} ---")
        print(f" Espécie: {self.especie}")
        print(f" Energia: {self.energia}")


# cachorro = Animal("Chucky", "Cachorro", "Au")
# gato = Animal("Kiko", "Gato", "oooooo")
# porco = Animal("Rodorfo", "Porco", "Oinc")
# lystorossaurus = Animal ("Maicon", "Vencedor", "Rusbé")

# gato.falar()
# cachorro.comer()
# cachorro.status()
# gato.status()

# lystorossaurus.falar()

# ─── HERANÇA ────────────────────────────────────────────────────
# Conceitos: herança, super(), override de método

class Cachorro(Animal):              # herda de Animal
    def __init__(self, nome, raca):
        super().__init__(nome, "Cachorro", "Au")
        self.raca = raca             # atributo novo, só do Cachorro

    def buscar(self, objeto):       # método novo
        print(f"{self.nome} buscou o(a) {objeto}! 🎾")

    def status(self):               # sobrescreve (override)
        super().status()             # chama o status do Animal
        print(f"  Raça    : {self.raca}")


class Gato(Animal):
    def __init__(self, nome, indoor):
        super().__init__(nome, "Gato", "Miau")
        self.indoor = indoor         # True = gato de interior

    def arranhar(self, alvo):
        print(f"{self.nome} arranhou {alvo}! 😾")


# ── Testando ────────────────────────────────────────────────────
rex  = Cachorro("Rex",  "Golden Retriever")
mia  = Gato("Mia",    True)

rex.falar()              # herdado de Animal
rex.buscar("bolinha")   # específico de Cachorro
rex.status()             # override

mia.falar()
mia.arranhar("o sofá")
mia.comer()              # herdado de Animal

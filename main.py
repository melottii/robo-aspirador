import random


class Agente:
    def __init__(self):
        self.localizacao = ["A", 0]
        self.posicoes_limpas = []
        self.limpar = False
        self.andar = False

    def __mostra_acao__(self):
        print(f"ONDE ESTOU: {'A' if self.localizacao[1] == 0 else 'B'}")
        print(f"LIMPEI O BLOCO? {'SIM' if self.limpar else 'NÃO'}")
        print(f"ANDEI? {'SIM' if self.andar else 'NÃO'}")
        print(f"POSICOES LIMPAS? {self.posicoes_limpas}")

    def __verifica_acao__(self, casa):
        if casa.sujo[self.localizacao[0]]:
            casa = Agente.__limpar__(self=self, casa=casa)
            Agente.__mostra_acao__(self=self)
        else:
            Agente.__mudar_posicao__(self=self)
            Agente.__mostra_acao__(self=self)
        return casa

    def __mudar_posicao__(self):
        self.limpar = False
        self.andar = True
        if self.andar and self.localizacao[1] == 0:
            self.localizacao[0], self.localizacao[1] = "B", 1
        elif self.andar:
            self.localizacao[0], self.localizacao[1] = "A", 0

    def __limpar__(self, casa):
        self.limpar = True
        self.andar = False
        self.posicoes_limpas.append(self.localizacao[0])
        casa.sujo[self.localizacao[0]] = False
        return casa


class Ambiente:
    def __init__(self):
        self.blocos = {"A": 0, "B": 1}
        self.sujo = {"A": False, "B": False}

    def __mostra_ambiente__(self, robo):
        print(f"{robo}: SITUAÇÃO DA CASA - {self.sujo}")


class Sujador:
    @staticmethod
    def __sujar_bloco__(casa, robo):
        if not casa.sujo["A"] and not casa.sujo["B"]:
            if robo.localizacao[0] == "A":
                casa.sujo["B"] = True
            else:
                casa.sujo["A"] = True
        elif casa.sujo["A"] and not casa.sujo["B"] and robo.localizacao[0] == "A":
            casa.sujo["B"] = True
        elif not casa.sujo["A"] and casa.sujo["B"] and robo.localizacao[0] == "B":
            casa.sujo["A"] = True
        return casa


if __name__ == "__main__":
    casa = Ambiente()
    sujador = Sujador()
    robo = Agente()

    #while True:
    for i in range(10):
        casa = sujador.__sujar_bloco__(casa=casa, robo=robo)
        print("SUJADOR: ", casa.sujo)
        casa = robo.__verifica_acao__(casa=casa)
        print("LIMPADOR: ", casa.sujo, "\n")

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

    def __verifica_acao__(self, casa_limpador):
        if casa_limpador.sujo[self.localizacao[0]]:
            casa_limpador = Agente.__limpar__(self=self, casa_limpador=casa_limpador)
            Agente.__mostra_acao__(self=self)
        else:
            Agente.__mudar_posicao__(self=self)
            Agente.__mostra_acao__(self=self)
        return casa_limpador

    def __mudar_posicao__(self):
        self.limpar = False
        self.andar = True
        if self.andar and self.localizacao[1] == 0:
            self.localizacao[0], self.localizacao[1] = "B", 1
        elif self.andar:
            self.localizacao[0], self.localizacao[1] = "A", 0

    def __limpar__(self, casa_limpador):
        self.limpar = True
        self.andar = False
        self.posicoes_limpas.append(self.localizacao[0])
        casa_limpador.sujo[self.localizacao[0]] = False
        return casa_limpador


class Ambiente:
    def __init__(self):
        self.blocos = {"A": 0, "B": 1}
        self.sujo = {"A": False, "B": False}

    def __mostra_ambiente__(self, modulo):
        print(f"{modulo}: SITUAÇÃO DA CASA - {self.sujo}")


class Sujador:
    @staticmethod
    def __sujar_bloco__(casa_sujador, limpador):
        if not casa_sujador.sujo["A"] and not casa_sujador.sujo["B"]:
            if limpador.localizacao[0] == "A":
                casa_sujador.sujo["B"] = True
            else:
                casa_sujador.sujo["A"] = True
        elif casa_sujador.sujo["A"] and not casa_sujador.sujo["B"] and limpador.localizacao[0] == "A":
            casa_sujador.sujo["B"] = True
        elif not casa_sujador.sujo["A"] and casa_sujador.sujo["B"] and limpador.localizacao[0] == "B":
            casa_sujador.sujo["A"] = True
        return casa_sujador


if __name__ == "__main__":
    casa = Ambiente()
    sujador = Sujador()
    robo = Agente()

    # while True:
    for i in range(10):
        casa = sujador.__sujar_bloco__(casa_sujador=casa, limpador=robo)
        casa.__mostra_ambiente__(modulo="SUJADOR")
        casa = robo.__verifica_acao__(casa_limpador=casa)
        casa.__mostra_ambiente__(modulo="LIMPADOR")
        print()

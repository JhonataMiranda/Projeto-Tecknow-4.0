import random


class roleta:

    def __init__(self, max):
        self.total_roleta = 100
        self.total = [100 for i in range(max)]
        self.porcentagem = self.total_roleta/max
        self.tam_max_roleta = max
        self.possibilidades = [True for x in range(max)]
        self.roleta = [self.porcentagem * (i+1) for i in range(max)]
        self.fracao_roleta = [self.porcentagem for i in range(max)]
        self.peso = self.total_roleta * 0.05

    def atualizar_roleta(self, i):
        self.fracao_roleta[i] += self.peso

        contador = 0
        diminuidor = 0

        for j in range(self.tam_max_roleta):
            if (j != i):
                if self.fracao_roleta[j] < 5:
                    contador += 1
                    diminuidor += self.fracao_roleta[j]
        if (not (self.fracao_roleta[i] + diminuidor > 100)):
            sub = self.peso / (self.tam_max_roleta - 1 - contador)
            #print("valor a ser retirado", sub)
            for j in range(self.tam_max_roleta):
                if self.fracao_roleta[j] > 5:
                    if j != i:
                        self.fracao_roleta[j] -= sub
        else:
            self.fracao_roleta[i] -= self.peso

        for j in range(self.tam_max_roleta):
            if j == 0:
                self.roleta[j] = self.fracao_roleta[j]
            else:
                self.roleta[j] = self.fracao_roleta[j] + self.roleta[j-1]

    def decrementar_roleta(self, i):
        if not (self.fracao_roleta[i] < self.peso):
            self.fracao_roleta[i] -= self.peso
            soma = self.peso / (self.tam_max_roleta - 1)
            for j in range(self.tam_max_roleta):
                if j != i:
                    self.fracao_roleta[j] += soma
            for j in range(self.tam_max_roleta):
                if j == 0:
                    self.roleta[j] = self.fracao_roleta[j]
                else:
                    self.roleta[j] = self.fracao_roleta[j] + self.roleta[j-1]\


    def resetar_possibilidades(self):
        self.possibilidades = [True for x in range(self.tam_max_roleta)]

    def retirar_possibilidade(self, k):
        self.possibilidades[k] = False

    def sortear(self):
        return random.uniform(0, 100)

    # TODO não usar recursividade, retornar posição sorteada
    def roletaAprendizado(self):

        valor = self.sortear()
        pos = 0
        #print("primeiro valor sorteado", valor)
        while self.roleta[pos] < valor:
            pos += 1
        if (self.possibilidades[pos] == False):
            while (True):
                pos = 0
                valor = self.sortear()
                # print("valor sorteado",valor)
                while self.roleta[pos] < valor:
                    pos += 1
                # print("posicao testada", pos)
                #pause = int(input())
                if (self.possibilidades[pos] == True):
                    break
        # print("posicao sorteada", pos)
        # print("porcentagens", self.fracao_roleta)
        # print("roleta", self.roleta)
        # print("possibilidades", self.possibilidades)
        # print("valor retornado", valor)
        return pos

    # TODO verificar esse algoritmo
    def maxRoleta(self):
        if self.possibilidades[self.fracao_roleta.index(max(self.fracao_roleta))]:
            return self.fracao_roleta.index(max(self.fracao_roleta))

    def epsilonGreedyAL(self, melhorou):
        return self.roletaAprendizado() if melhorou else self.maxRoleta()

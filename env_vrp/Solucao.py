from env_vrp.Roteamento import Roteamento
from env_vrp.Rota import Rota


class Solucao:
    """
    Classe que representa uma solução para o problema de roteamento de veículos

    Atributos
    ----------
    numero_rotas : int 
        representa o número de rotas criadas para solucionar o problema
    vetor_solucao : Rota
        vetor que armazena todas as rotas criadas para resolver o problema 
    funcao_objetivo_tempo : float
        representa o valor da função objetivo calculada em função do tempo gasto para deslocar entre clientes
    custo_sem_penalidade_tempo : float
        representa o valor da função objetivo calculada em função do tempo gasto para deslocar entre clientes
        excluindo a penalidade aplicada ao inserir uma nova rota
    funcao_objetivo_distancia : float
        representa o valor da função objetivo calculada em função da distância percorrida para deslocar entre
        clientes
    custo_sem_penalidade_distancia : float
        representa o valor da função objetivo calculada em função da distância percorrida para deslocar entre
        clientes excluindo a penalidade aplicada ao inserir uma nova rota

    Métodos
    -------
    calcula_funcao_objetivo_tempo()
        calcula valor da função objetivo considerando o tempo gasto para deslocar entre clientes
    calcula_funcao_objetivo_distancia()
        calcula valor da função objetivo considerando a distância percorrida para deslocar entre clientes
    copia()
        copia os valores de um cliente para outro
    exibe()
        mostra no terminal todos os dados de um cliente
    """

    def __init__(self):
        """ Inicializa todas as variáveis da classe como 0 e o vetor como vazio
        Parâmetros
        ----------
        Nenhum
        """
        self.numero_rotas = 0
        self.vetor_solucao = []
        self.funcao_objetivo_tempo = 0.0
        self.custo_sem_penalidade_tempo = 0.0
        self.funcao_objetivo_distancia = 0.0
        self.custo_sem_penalidade_distancia = 0.0

    # calcula a função objetivo de uma rota, com base na distancia entre clientes
    def calcula_funcao_objetivo_distancia(self, roteamento):
        """ Calcula o valor da função objetivo, com e sem penalidade, fazendo 
        a soma do tempo total de cada uma das rotas

        Parâmetros
        ----------
        roteamento : roteamento 
            representa o problema de roteamento com os dados a serem utilizados

        Retorno
        ------
        Nenhum
        """
        custo = 0
        for j in range(len(self.vetor_solucao)):
            custo = custo + self.vetor_solucao[j].distancia_total
        self.custo_sem_penalidade_distancia = custo
        custo = custo + self.numero_rotas * roteamento.penalidade_veiculo
        self.funcao_objetivo_distancia = custo

    # calcula a função objetivo de uma rota, com base no tempo entre clientes
    def calcula_funcao_objetivo_tempo(self, roteamento):
        """ Calcula o valor da função objetivo, com e sem penalidade, fazendo 
        a soma da distância total de cada uma das rotas

        Parâmetros
        ----------
        roteamento : roteamento 
            representa o problema de roteamento com os dados a serem utilizados

        Retorno
        ------
        Nenhum
        """
        custo = 0
        for j in range(0, self.numero_rotas):
            custo += self.vetor_solucao[j].tempo_total
        self.custo_sem_penalidade_tempo = custo
        custo = custo + self.numero_rotas * roteamento.penalidade_veiculo
        self.funcao_objetivo_tempo = custo

        # podemos remover depois
        self.calcula_funcao_objetivo_distancia(roteamento)

    # copia uma solução para outra
    def copia(self, solucao, janela_final):
        """Copia os atributos de uma solução para outra, copiando rota a rota.

        Parâmetros
        ----------
        solucao : Solucao
            solucao vazia para armazenar os dados a serem copiados

        Retorno
        ------
        Nenhum
        """
        self.numero_rotas = solucao.numero_rotas
        self.vetor_solucao.clear()
        for i in range(self.numero_rotas):
            rota_aux = Rota(janela_final)
            rota_aux = solucao.vetor_solucao[i].copia(janela_final)
            self.vetor_solucao.append(rota_aux)
        self.funcao_objetivo_tempo = solucao.funcao_objetivo_tempo
        self.custo_sem_penalidade_tempo = solucao.custo_sem_penalidade_tempo
        self.funcao_objetivo_distancia = solucao.funcao_objetivo_distancia
        self.custo_sem_penalidade_distancia = solucao.custo_sem_penalidade_distancia

    def exibe(self):
        """Exibe os dados da solução no terminal.

        Parâmetros
        ----------
        Nenhum

        Retorno
        ------
        Nenhum
        """
        print("Solução:")
        print("Função objetivo tempo: ", self.funcao_objetivo_tempo)
        print("Custo sem penalidade tempo: ", self.custo_sem_penalidade_tempo)
        print("Função objetivo distancia: ", self.funcao_objetivo_distancia)
        print("Custo sem penalidade distancia: ",
              self.custo_sem_penalidade_distancia)
        print("Número de rotas: ", self.numero_rotas)
        print("Rotas:")
        for i in range(0, self.numero_rotas):
            print()
            print("Rota: ", i+1)
            print("Tamanho rota: ", len(self.vetor_solucao[i].rota))
            print()
            self.vetor_solucao[i].exibe()
            print("----------------------------------------\n")

    # MOVIMENTOS

    def swapIntra(self, rota1, posicao1, posicao2, roteamento):
        """ Verifica a possibilidade de realizar uma troca entre dois clientes numa mesma rota.
        O cliente na posicao1 passa a ocupar a posicao2 e o cliente na posicao2 passa a ocupar a posicao1. 
        Após a troca, verifica se a nova rota atende as restrições do problema

        Parâmetros
        ----------
        rota1: Rota
            rota que terá seus clientes trocados
        posicao1: int
            posição do primeiro cliente da rota
        posicao2: int
            posição do seguindo cliente da rota
        roteamento : roteamento 
            representa o problema de roteamento com os dados a serem utilizados 
        Retorno
        ------
        Retorna um booleano com True caso a troca possa ser realizada ou False caso contrário
        """
        if posicao1 == posicao2:
            return True
        elif len(self.vetor_solucao[rota1].rota) < 2:
            return False
        else:
            cliente1 = self.vetor_solucao[rota1].rota[posicao1]
            cliente2 = self.vetor_solucao[rota1].rota[posicao2]

            if posicao1 < posicao2:
                self.vetor_solucao[rota1].remover_cliente(
                    cliente2, roteamento, posicao2)
                self.vetor_solucao[rota1].remover_cliente(
                    cliente1, roteamento, posicao1)
                self.vetor_solucao[rota1].adiciona_cliente(
                    cliente2, roteamento, posicao1)
                self.vetor_solucao[rota1].adiciona_cliente(
                    cliente1, roteamento, posicao2)
            if posicao2 < posicao1:
                self.vetor_solucao[rota1].remover_cliente(
                    cliente1, roteamento, posicao1)
                self.vetor_solucao[rota1].remover_cliente(
                    cliente2, roteamento, posicao2)
                self.vetor_solucao[rota1].adiciona_cliente(
                    cliente1, roteamento, posicao2)
                self.vetor_solucao[rota1].adiciona_cliente(
                    cliente2, roteamento, posicao1)

            # verificar restrições
            if self.vetor_solucao[rota1].comparar_tempo() == False:
                return False
        return True

    def swapInter(self, rota1, posicao1, rota2, posicao2, roteamento):
        """ Verifica a possibilidade de realizar uma troca entre dois clientes em rotas diferentes.
        O cliente na posicao1 da rota1 passa a ocupar a posicao2 da rota2 e o cliente na posicao2
        da rota2 passa a ocupar a posicao1 da rota1. 
        Após a troca, verifica se as novas rotas atendem as restrições do problema

        Parâmetros
        ----------
        rota1: Rota
            primeira rota que terá seus clientes trocados
        rota2: Rota
            segunda rota que terá seus clientes trocados
        posicao1: int
            posição do primeiro cliente da rota1
        posicao2: int
            posição do seguindo cliente da rota2
        roteamento : roteamento 
            representa o problema de roteamento com os dados a serem utilizados 
        Retorno
        ------
        Retorna um booleano com True caso a troca possa ser realizada ou False caso contrário
        """
        if rota1 == rota2 and posicao1 == posicao2:
            return True
        elif len(self.vetor_solucao[rota1].rota) < 2 or len(self.vetor_solucao[rota2].rota) < 2:
            return False
        else:
            cliente1 = self.vetor_solucao[rota1].rota[posicao1]
            cliente2 = self.vetor_solucao[rota2].rota[posicao2]
            self.vetor_solucao[rota1].remover_cliente(
                cliente1, roteamento, posicao1)
            self.vetor_solucao[rota2].remover_cliente(
                cliente2, roteamento, posicao2)
            self.vetor_solucao[rota2].adiciona_cliente(
                cliente1, roteamento, posicao2)
            self.vetor_solucao[rota1].adiciona_cliente(
                cliente2, roteamento, posicao1)

            # verificar restrições
            if roteamento.capacidade_veiculos[rota1] < self.vetor_solucao[rota1].demanda_total or roteamento.capacidade_veiculos[rota2] < self.vetor_solucao[rota2].demanda_total:
                return False
            if (self.vetor_solucao[rota1].comparar_tempo() == False) or (self.vetor_solucao[rota2].comparar_tempo() == False):
                return False
        return True

    def shiftIntra(self, rota1, posicao1, posicao2, roteamento):
        """ Verifica a possibilidade de realizar uma inserção de um cliente que estava
        em uma posição em outra posição na mesma rota. O cliente na posicao1 passa a ocupar
        a posicao2 e o todos os clientes subsequentes passam a ocupar uma posição frente da sua posição atual. 
        Após a troca, verifica se a nova rota atende as restrições do problema

        Parâmetros
        ----------
        rota1: Rota
            rota que terá seu cliente reinserido
        posicao1: int
            posição inicial do cliente da rota
        posicao2: int
            posição final do cliente da rota
        roteamento : roteamento 
            representa o problema de roteamento com os dados a serem utilizados 
        Retorno
        ------
        Retorna um booleano com True caso a troca possa ser realizada ou False caso contrário
        """
        if posicao1 == posicao2:
            return True
        elif len(self.vetor_solucao[rota1].rota) < 2:
            return False
        else:
            cliente1 = self.vetor_solucao[rota1].rota[posicao1]
            self.vetor_solucao[rota1].remover_cliente(
                cliente1, roteamento, posicao1)
            self.vetor_solucao[rota1].adiciona_cliente(
                cliente1, roteamento, posicao2)

        # verificar restrições
        if self.vetor_solucao[rota1].comparar_tempo() == False:
            return False
        return True

    def shiftInter(self, rota1, posicao1, rota2, posicao2, roteamento):
        """ Verifica a possibilidade de realizar uma inserção de um cliente que estava
        em uma posição em outra posição em uma outra rota. O cliente na posicao1 da rota de origem passa a ocupar
        a posicao2 da rota de destino e o todos os clientes subsequentes na rota de destino 
        passam a ocupar uma posição frente da sua posição atual. 
        Após a troca, verifica se a nova rota atende as restrições do problema

        Parâmetros
        ----------
        rota1: Rota
            rota de origem do cliente
        rota2: Rota
            rota de destino do cliente
        posicao1: int
            posição inicial do cliente da rota de origem
        posicao2: int
            posição final do cliente da rota de destino
        roteamento : roteamento 
            representa o problema de roteamento com os dados a serem utilizados 
        Retorno
        ------
        Retorna um booleano com True caso a troca possa ser realizada ou False caso contrário
        """
        if rota1 == rota2 and posicao1 == posicao2:
            return True
        elif len(self.vetor_solucao[rota1].rota) < 2:
            return False
        elif rota1 >= len(self.vetor_solucao) or rota2 >= len(self.vetor_solucao):
            return False
        else:
            cliente1 = self.vetor_solucao[rota1].rota[posicao1]
            self.vetor_solucao[rota1].remover_cliente(
                cliente1, roteamento, posicao1)
            self.vetor_solucao[rota2].adiciona_cliente(
                cliente1, roteamento, posicao2)
            # verificar restrições
            if (roteamento.capacidade_veiculos[rota1] < self.vetor_solucao[rota1].demanda_total) or (roteamento.capacidade_veiculos[rota2] < self.vetor_solucao[rota2].demanda_total):
                return False
            if (self.vetor_solucao[rota1].comparar_tempo() == False) or (self.vetor_solucao[rota2].comparar_tempo() == False):
                return False
        return True

    def nSwapInter(self, n, rota1, posicao1, rota2, posicao2, roteamento):
        """ Verifica a possibilidade de realizar uma troca entre n clientes de uma rota com n clientes de outra rota.
        Os n clientes a partir da posicao1 da rota1 passam a ocupar as n posições a partir posicao2 da rota2 e os n
        clientes a partir da posicao2 da rota2 passam a ocupar as n posições a partir da posicao1 da rota1. 
        Após a troca, verifica se as novas rotas atendem as restrições do problema

        Parâmetros
        ----------
        rota1: Rota
            primeira rota que terá seus clientes trocados
        rota2: Rota
            segunda rota que terá seus clientes trocados
        posicao1: int
            posição do primeiro dos n clientes da rota1
        posicao2: int
            posição do primeiro dos n clientes da rota2
        roteamento : roteamento 
            representa o problema de roteamento com os dados a serem utilizados 
        Retorno
        ------
        Retorna um booleano com True caso a troca possa ser realizada ou False caso contrário
        """
        count = 0
        if len(self.vetor_solucao[rota1].rota) <= n or len(self.vetor_solucao[rota2].rota) <= n:
            return False
        while count < n and posicao1 <= len(self.vetor_solucao[rota1].rota) and posicao2 <= len(self.vetor_solucao[rota2].rota):
            if rota1 == rota2 and posicao1 == posicao2:
                return True
            else:
                cliente1 = self.vetor_solucao[rota1].rota[posicao1]
                cliente2 = self.vetor_solucao[rota2].rota[posicao2]
                self.vetor_solucao[rota1].remover_cliente(
                    cliente1, roteamento, posicao1)
                self.vetor_solucao[rota2].remover_cliente(
                    cliente2, roteamento, posicao2)
                self.vetor_solucao[rota2].adiciona_cliente(
                    cliente1, roteamento, posicao2)
                self.vetor_solucao[rota1].adiciona_cliente(
                    cliente2, roteamento, posicao1)

                # verificar restrições
                if (roteamento.capacidade_veiculos[rota1] < self.vetor_solucao[rota1].demanda_total) or (roteamento.capacidade_veiculos[rota2] < self.vetor_solucao[rota2].demanda_total):
                    return False
                if (self.vetor_solucao[rota1].comparar_tempo() == False) or (self.vetor_solucao[rota2].comparar_tempo() == False):
                    return False

                posicao1 += 1
                posicao2 += 1
                count += 1
        return True

    def nShiftInter(self, n, rota1, posicao1, rota2, posicao2, roteamento):
        """ Verifica a possibilidade de realizar uma inserção de n clientes que estavam
        em n posições a partir da posicao1 em outras n posições a partir da posicao2 em uma outra rota.
        Os n clientes a partir da posicao1 da rota de origem passam a ocupar as n posições a partir da posicao2
        da rota de destino e o todos os clientes subsequentes na rota de destino 
        passam a ocupar n posições frente da sua posição atual. 
        Após a troca, verifica se a nova rota atende as restrições do problema

        Parâmetros
        ----------
        rota1: Rota
            rota de origem do cliente
        rota2: Rota
            rota de destino do cliente
        posicao1: int
            posição do primeiro dos n clientes da rota1
        posicao2: int
            posição do primeiro dos n clientes da rota2
        roteamento : roteamento 
            representa o problema de roteamento com os dados a serem utilizados 
        Retorno
        ------
        Retorna um booleano com True caso a troca possa ser realizada ou False caso contrário
        """
        count = 0
        if len(self.vetor_solucao[rota1].rota) <= n:
            return False
        while count < n and posicao1 <= len(self.vetor_solucao[rota1].rota) and posicao2 <= len(self.vetor_solucao[rota2].rota):
            if rota1 == rota2 and posicao1 == posicao2:
                return True
            elif rota1 >= len(self.vetor_solucao) or rota2 >= len(self.vetor_solucao):
                return False
            else:
                cliente1 = self.vetor_solucao[rota1].rota[posicao1]
                self.vetor_solucao[rota1].remover_cliente(
                    cliente1, roteamento, posicao1)
                self.vetor_solucao[rota2].adiciona_cliente(
                    cliente1, roteamento, posicao2)
                # verificar restrições
                if rota1 >= len(self.vetor_solucao) or rota2 >= len(self.vetor_solucao):
                    return False
                if (roteamento.capacidade_veiculos[rota1] < self.vetor_solucao[rota1].demanda_total) or (roteamento.capacidade_veiculos[rota2] < self.vetor_solucao[rota2].demanda_total):
                    return False
                if (self.vetor_solucao[rota1].comparar_tempo() == False) or (self.vetor_solucao[rota2].comparar_tempo() == False):
                    return False
                posicao2 += 1
                count += 1
        return True

    # testa a melhor posição para inserir o cliente em uma solução
    def testa_melhor_posicao_solucao(self, cliente, roteamento, sem_janela,rota_atual):
        janela_final = roteamento.colecao_clientes[0].janela_final
        # para cada rota, cria-se uma auxiliar
        for i in range(self.numero_rotas):
            if i != rota_atual:
                # recebe a melhor posição a se inserir numa rota
                # TODO verificar se o tempo de chegada + o tempo de viagem é menor que o tempo da janela final do cliente atual
                for j in range(len(self.vetor_solucao[i].rota)+1):
                    rota_aux = Rota(janela_final)
                    rota_aux = self.vetor_solucao[i].copia(janela_final)
                    rota_aux.adiciona_cliente(cliente, roteamento, j)
                    flag = rota_aux.comparar_tempo()
                    if flag == True:
                        return i,j
                    
        return -1, -1

    def eliminaMenorRota(self, roteamento):

        tamanhoMenor = float('inf')
        rotaMenor = -1
        # encontra a menor rota
        for i in range(self.numero_rotas):
            if len(self.vetor_solucao[i].rota) < tamanhoMenor:
                tamanhoMenor = len(self.vetor_solucao[i].rota)
                rotaMenor = i
        # tenta alocar seus clientes em outras rotas
        posicao1 = 0
        print("Menor rota: ",rotaMenor)
        print("Tamanho menor rota: ",len(self.vetor_solucao[rotaMenor].rota))
        print("quantidade rotas: ", self.numero_rotas)
        for cliente in self.vetor_solucao[rotaMenor].rota:
            # verifica melhor posição para se inserir cada cliente em alguma outra rota
            rota_insercao, posicao_insecao = self.testa_melhor_posicao_solucao(
                cliente, roteamento, True,rotaMenor)
            print("posicoes para o cliente :", posicao1,
                  posicao_insecao, rota_insercao)
            # se não encontrar nenhuma posição viável, retorna false
            if posicao_insecao == -1 or rota_insercao == -1:
                posicao1 += 1
                continue
                # return False, posicao1
            if len(self.vetor_solucao[rotaMenor].rota) > 1:
                self.vetor_solucao[rotaMenor].remover_cliente(
                    cliente, roteamento, posicao1)
                self.vetor_solucao[rota_insercao].adiciona_cliente(
                    cliente, roteamento, posicao_insecao)
            if len(self.vetor_solucao[rotaMenor].rota) == 1:
                self.vetor_solucao[rota_insercao].adiciona_cliente(
                    cliente, roteamento, posicao_insecao)
                self.vetor_solucao.pop(rotaMenor)
                self.numero_rotas -= 1
                return True
            if roteamento.capacidade_veiculos[rota_insercao] < self.vetor_solucao[rota_insercao].demanda_total:
                return False
            if self.vetor_solucao[rota_insercao].comparar_tempo() == False:
                return False
            posicao1 += 1
        return True

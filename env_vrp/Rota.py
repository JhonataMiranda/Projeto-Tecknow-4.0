import sys
from env_vrp import Roteamento


class Rota:
    """
    Classe que representa uma rota de clientes

    Atributos
    ----------
    rota : Cliente 
        um vetor que armazena os clientes na ordem em que serão atendidos
    tempo_atendimento : int
        um vetor que armazena os tempos em que cada cliente serão atendidos seguindo a ordem da rota
    demanda_total : int
        soma total das demandas de todos os clientes da rota
    tempo_total : int
        soma total do tempo gasto para atender todos os clientes da rota
    distancia_total : int
        soma total da distancia percorrida pela rota
    tempo_inicial : int
        tempo em que se inicia a rota
    tempo_final : int
        tempo em que se finaliza a rota

    Métodos
    -------
    atualizar_tempo_rota(roteamento)
        atualiza o tempo total de uma rota, o tempo de atendimento e a distância total percorrida
    melhor_posicao(cliente, roteamento)
        retorna qual a melhor posição para se inserir na rota, retorna -1 caso não exista
    comparar_tempo()
        verifica se a janela de tempo da rota não está sendo violada
    adiciona_cliente(cliente, roteamento, posicao)
        adiciona um cliente em determinada posição na rota
    copia()
        copia os valores de um cliente para outro
    exibe()
        mostra no terminal todos os dados de um cliente
    """

    def __init__(self,janela_final):
        """ Inicializa todas as variáveis da classe como 0 e os vetores como vazio
        Parâmetros
        ----------
        Nenhum
        """
        self.rota = []
        self.tempo_atendimento = []
        self.demanda_total = 0
        self.tempo_total = 0
        self.distancia_total = 0
        self.tempo_inicial = 0
        self.tempo_final = janela_final

    # atualiza o tempo da rota
    def atualizar_tempo_rota(self, roteamento):
        """ Atualiza o tempo que é gasto para percorrer uma rota após alterações feitas nela. Faz-se a verificação 
        das restrições do problema e só realiza a alteração caso seja viável.

        Parâmetros
        ----------
        roteamento : roteamento 
            representa o problema de roteamento com os dados a serem utilizados

        Retorno
        ------
        Nenhum
        """
        tempo_espera = 0
        self.tempo_total = 0
        self.tempo_atendimento.clear()

        # compara o tempo de atendimento do cliente com a janela inicial da rota
        if roteamento.matriz_custo_tempo[0][self.rota[0].id_cliente] < self.rota[0].janela_inicial:
            tempo_espera += self.rota[0].janela_inicial - \
                roteamento.matriz_custo_tempo[0][self.rota[0].id_cliente]
            self.tempo_total = self.rota[0].janela_inicial
        else:
            self.tempo_total = roteamento.matriz_custo_tempo[0][self.rota[0].id_cliente]

        self.distancia_total = roteamento.matriz_custo_distancia[0][self.rota[0].id_cliente]
        self.tempo_atendimento.append(self.tempo_total)
        self.tempo_total += roteamento.colecao_clientes[self.rota[0].id_cliente].tempo_atendimento
        for i in range(1, len(self.rota)):
            if (self.tempo_total + roteamento.matriz_custo_tempo[self.rota[i-1].id_cliente][self.rota[i].id_cliente]) < self.rota[i].janela_inicial:
                tempo_espera += self.rota[i].janela_inicial - \
                    roteamento.matriz_custo_tempo[self.rota[i -
                                                            1].id_cliente][self.rota[i].id_cliente]
                self.tempo_total = self.rota[i].janela_inicial
            else:
                self.tempo_total += roteamento.matriz_custo_tempo[self.rota[i -
                                                                            1].id_cliente][self.rota[i].id_cliente]
            self.tempo_atendimento.append(self.tempo_total)

            self.tempo_total += self.rota[i].tempo_atendimento
            self.distancia_total += roteamento.matriz_custo_distancia[self.rota[i -
                                                                                1].id_cliente][self.rota[i].id_cliente]

        self.tempo_total += roteamento.matriz_custo_tempo[self.rota[len(
            self.rota)-1].id_cliente][0]
        self.distancia_total += roteamento.matriz_custo_distancia[self.rota[len(
            self.rota)-1].id_cliente][0]

    def melhor_posicao(self, cliente, roteamento):
        """ Atualiza o tempo que é gasto para percorrer uma rota após alterações feitas nela. Faz-se a verificação 
        das restrições do problema e só realiza a alteração caso seja viável.

        Parâmetros
        ----------
        cliente : cliente
            representa o cliente que deve ser inserido em uma rota
        roteamento : roteamento 
            representa o problema de roteamento com os dados a serem utilizados

        Retorno
        ------
        posicao_min : int
            é a melhor posição encontrada ao percorrer a rota para se inserir o cliente
        """
        min = sys.float_info.max
        posicao_min = -1
        janela_final = roteamento.colecao_clientes[0].janela_final
        for i in range(len(self.rota)+1):
            # print("pos na rota", i)
            rota_aux = Rota(janela_final)
            rota_aux = self.copia(janela_final)
            rota_aux.adiciona_cliente(cliente, roteamento, i)
            flag = rota_aux.comparar_tempo()
            if flag == True:
                if min > rota_aux.tempo_total:
                    min = rota_aux.tempo_total
                    posicao_min = i
        return posicao_min

    def comparar_tempo(self):
        """ Verifica se realizar o atendimento de um cliente 

        Parâmetros
        ----------
        Nenhum

        Retorno
        ------
        Retorna um booleano com True caso a rota atual extrapole a janela de tempo
        final do problema ou False caso contrário
        """

        for i in range(len(self.rota)):
            # se o cliente está sendo atendido no fim da janela da rota ou posteriormente, ele não pode ser inserido
            if self.tempo_final <= self.tempo_atendimento[i]:
                return False
        
        return True

    def adiciona_cliente(self, cliente, roteamento, posicao):
        """ Adiciona um cliente em uma rota em uma posição específica e faz solicita a alteração do tempo da rota.

        Parâmetros
        ----------
        cliente : cliente
            representa o cliente que deve ser inserido em uma rota
        roteamento : roteamento 
            representa o problema de roteamento com os dados a serem utilizados
        posicao : int
            representa a posição da rota que se deseja inserir o cliente     

        Retorno
        ------
        Nenhum
        """
        self.rota.insert(posicao, cliente)
        self.demanda_total += cliente.demanda
        self.atualizar_tempo_rota(roteamento)

    def remover_cliente(self, cliente, roteamento, posicao):
        """ Remove um cliente em uma rota em uma posição específica e faz solicita a alteração do tempo da rota.

        Parâmetros
        ----------
        cliente : cliente
            representa o cliente que deve ser inserido em uma rota
        roteamento : roteamento 
            representa o problema de roteamento com os dados a serem utilizados
        posicao : int
            representa a posição da rota que se deseja inserir o cliente     

        Retorno
        ------
        Nenhum
        """    
        self.rota.pop(posicao)
        self.demanda_total-= cliente.demanda
        self.atualizar_tempo_rota(roteamento)

    # copiar uma rota para outra
    def copia(self,janela_final):
        """Copia os atributos de uma rota para outra.

        Parâmetros
        ----------
        Nenhum

        Retorno
        ------
        rota : Rota
            Retorna uma rota com os dados copiados
        """
        rota = Rota(janela_final)
        rota.rota = self.rota.copy()
        rota.demanda_total = self.demanda_total
        rota.tempo_total = self.tempo_total
        rota.tempo_inicial = self.tempo_inicial
        rota.tempo_final = self.tempo_final
        return rota

    
    # exibir uma rota
    def exibe(self):
        """Exibe os dados da rota no terminal.

        Parâmetros
        ----------
        Nenhum

        Retorno
        ------
        Nenhum
        """
        print("Rota: ")
        for i in range(len(self.rota)):
            print("ID do cliente: ",self.rota[i].id_cliente)
            print("Tempo de atemdimento do cliente: ",self.tempo_atendimento[i])
        print()
        print("Demanda da rota: ", self.demanda_total)
        print("Tempo da rota: ", self.tempo_total)
        print("Distancia da rota:",self.distancia_total)
        print("Janela de tempo inicial da rota: ", self.tempo_inicial)
        print("Janela de tempo final da rota: ", self.tempo_final)

        print("---------------------------------------------------------")

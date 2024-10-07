from env_vrp.Solucao import Solucao
from env_vrp.Solucao import Rota
import sys


import math


class Elemento_Construcao_VRP:
    def __init__(self):
        self.candidatos = []
        self.posicao_candidato = 0
        self.clientes_nao_inseridos = 0
        self.rota_insercao = 0
        self.posicao_insecao = 0
        self.proximo_candidato = -1
        self.custo_insercao = []
        self.lrc = []

    # inicializa os candidatos e enquanto houver candidatos, insere o primeiro na solução

    def constroi(self, roteamento,sem_janela):
        s = Solucao()
        # self.inicializa_candidatos(roteamento)
        for i in range(1,len(roteamento.colecao_clientes)):
            proximo = roteamento.colecao_clientes[i]
            # print("cliente a inserir: ",proximo.id_cliente)
            self.adiciona_cliente_em_solucao(roteamento, proximo, s,sem_janela)
        return s


    # inicializa os clientes de acordo com seu custo de inserção, em ordem crescente
    def inicializa_candidatos(self, roteamento):
        roteamento.colecao_clientes.sort(key=lambda cliente: cliente.janela_inicial)

    # testa a melhor posição para inserir o cliente em uma solução
    def testa_melhor_posicao_solucao(self, cliente, solucao, roteamento,sem_janela):
        self.posicao_insecao = -1
        self.rota_insercao = -1
        posicao = 0
        min = sys.float_info.max
        janela_final = roteamento.colecao_clientes[0].janela_final
        # para cada rota, cria-se uma auxiliar
        for i in range(solucao.numero_rotas):
            solucao_aux = Solucao()
            solucao_aux.copia(solucao,janela_final)
            # recebe a melhor posição a se inserir numa rota
            #TODO verificar se o tempo de chegada + o tempo de viagem é menor que o tempo da janela final do cliente atual
            posicao = solucao_aux.vetor_solucao[i].melhor_posicao(
                cliente, roteamento)
            # se a posição é valida, insere e calcula a função objetivo
            #TODO aceitar melhor solução de acordo com a função objetivo quando tiver a instancia que não tem janela de tempo nos clientes
            if posicao != -1:
                if sem_janela:
                    solucao_aux.calcula_funcao_objetivo_tempo(roteamento)
                    if solucao_aux.funcao_objetivo_tempo < min:
                        min = solucao_aux.funcao_objetivo_tempo
                        self.rota_insercao = i
                        self.posicao_insecao = posicao
                else:
                    solucao_aux.vetor_solucao[i].adiciona_cliente(
                    cliente, roteamento, posicao)
                    self.rota_insercao = i
                    self.posicao_insecao = posicao
                    break

                
        if self.rota_insercao == -1 or self.posicao_insecao == -1:
            return False
        else:
            return True

    # adiciona o cliente  em uma solução
    def adiciona_cliente_em_solucao(self, roteamento, cliente, solucao,sem_janela):
        # se não houver rotas, cria uma nova e adiciona o cliente
        if solucao.numero_rotas == 0:
            nova_rota = Rota(roteamento.colecao_clientes[0].janela_final)
            nova_rota.adiciona_cliente(cliente, roteamento, 0)
            solucao.vetor_solucao.append(nova_rota)
            solucao.numero_rotas += 1
            # print("Cria rota ",solucao.numero_rotas)
        # se houver, testa a melhor posição para inserir o cliente na rota
        elif (self.testa_melhor_posicao_solucao(cliente, solucao, roteamento,sem_janela)) == True:
            # print("Cliente inserido na rota ", self.rota_insercao+1, "na posicao ", self.posicao_insecao)
            solucao.vetor_solucao[self.rota_insercao].adiciona_cliente(
                cliente, roteamento, self.posicao_insecao)
            solucao.vetor_solucao[self.rota_insercao].atualizar_tempo_rota(
                roteamento)
            # print(solucao.vetor_solucao[self.rota_insercao].tempo_atendimento)
        # elif solucao.numero_rotas < roteamento.numero_veiculos:
        else:
            # caso não seja possivel, insere o cliente em uma nova rota
            nova_rota = Rota(roteamento.colecao_clientes[0].janela_final)
            nova_rota.adiciona_cliente(cliente, roteamento, 0)
            solucao.vetor_solucao.append(nova_rota)
            solucao.numero_rotas += 1
            # print("Cria rota ",solucao.numero_rotas)
        # else:  
        #     #insere na menor rota existente
        #     print("++++++++++++++++++++++++++++++++")
        #     print("Cliente ", cliente.id_cliente,"não pode ser inserido em nenhuma rota")
        #     self.clientes_nao_inseridos += 1
            # min = len(solucao.vetor_solucao[0].rota)
            # rota_min = 0
            # for i in range(1,solucao.numero_rotas):
            #     if len(solucao.vetor_solucao[i].rota) < min:
            #         min = len(solucao.vetor_solucao[i].rota)
            #         rota_min = i
            # posicao_insercao = solucao.vetor_solucao[rota_min].melhor_posicao(cliente,roteamento)
            # solucao.vetor_solucao[rota_min].adiciona_cliente(cliente,roteamento,posicao_insercao)
        

    


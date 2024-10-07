from env_vrp.Roteamento import Roteamento
from env_vrp.Solucao import Solucao
from busca_local_vrp.VND import VND
from const_vrp.Elemento_Construcao_VRP import Elemento_Construcao_VRP
from aprendizado.roleta import roleta
import time


def main():
    print("Realizando leitura dos dados!")
    time.sleep(5)
    sem_janela = True
    # path = 'data/instanciaRealHidrosabor.txt'
    path = 'data/instanciaRealHidrosabor_semJanela.txt'
    roteamento = Roteamento(path,isreal=True)
    construtor_problema = Elemento_Construcao_VRP()
    solucao = Solucao()
    solucao = construtor_problema.constroi(roteamento,sem_janela)
    print("Numero de clientes nao inseridos: ",construtor_problema.clientes_nao_inseridos)
    solucao.calcula_funcao_objetivo_tempo(roteamento)
    solucao.exibe()
    print("Construindo conjunto de rotas!!")
    vnd = VND()
    vnd.VND(roteamento,solucao)
    for i in range (len(vnd.solucao_melhorada.vetor_solucao)):
        vnd.solucao_melhorada.vetor_solucao[i].atualizar_tempo_rota(roteamento)
    vnd.solucao_melhorada.calcula_funcao_objetivo_distancia(roteamento)
    vnd.solucao_melhorada.exibe()


main()

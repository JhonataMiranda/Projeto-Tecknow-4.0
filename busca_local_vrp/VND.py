from busca_local_vrp.Primeiro_Melhora import Primeiro_Melhora   
from env_vrp.Solucao import Solucao
from aprendizado.roleta import roleta
    
    
class VND:
    def __init__(self):
        self.busca_local = Primeiro_Melhora()
        self.k = 0
        self.qt_vizinhancas = 7
        self.melhorou = True
        self.qt_visitados = 0
        self.roleta = roleta(self.qt_vizinhancas)
        self.solucao_melhorada = Solucao()

    def VND(self,roteamento,solucao_inicial):
        janela_final = roteamento.colecao_clientes[0].janela_final
        self.solucao_melhorada.copia(solucao_inicial,janela_final)
        qt_tentativas = 50
        while(self.qt_visitados < 7):
            self.k = self.roleta.epsilonGreedyAL(self.melhorou)
            print("Valor do k do VND",self.k)
            match self.k:
                case 0:
                    self.solucao_melhorada.copia(self.busca_local.primeiro_melhora_swap_intra(solucao_inicial,roteamento),janela_final)
                case 1:
                    self.solucao_melhorada.copia(self.busca_local.primeiro_melhora_shift_intra(solucao_inicial,roteamento),janela_final)
                case 2:
                    self.solucao_melhorada.copia(self.busca_local.primeiro_melhora_swap_inter(solucao_inicial,roteamento),janela_final)
                case 3:
                    self.solucao_melhorada.copia(self.busca_local.primeiro_melhora_shift_inter(solucao_inicial,roteamento),janela_final)
                case 4:
                    self.solucao_melhorada.copia(self.busca_local.primeiro_melhora_n_swap_inter(solucao_inicial,roteamento),janela_final)
                case 5:
                    self.solucao_melhorada.copia(self.busca_local.primeiro_melhora_n_shift_inter(solucao_inicial,roteamento),janela_final)
                case 6:
                    self.solucao_melhorada.copia(self.busca_local.primeiro_melhora_remove_menor_rota(solucao_inicial,roteamento),janela_final)    
            self.solucao_melhorada.calcula_funcao_objetivo_distancia(roteamento)
            self.solucao_melhorada.calcula_funcao_objetivo_tempo(roteamento)
            if self.k != 6 or qt_tentativas == 0:
                # print("Objts:",self.solucao_melhorada.funcao_objetivo_tempo," ",solucao_inicial.funcao_objetivo_tempo)
                if qt_tentativas == 0:
                    print("nao melhorou")
                    self.roleta.decrementar_roleta(self.k)
                    self.qt_visitados += 1
                    self.roleta.retirar_possibilidade(self.k)
                elif self.solucao_melhorada.funcao_objetivo_tempo < solucao_inicial.funcao_objetivo_tempo:
                    print("melhorou")
                    solucao_inicial.copia(self.solucao_melhorada,janela_final)
                    self.melhorou = True
                    self.qt_visitados = 0
                    self.roleta.atualizar_roleta(self.k)
                    self.roleta.resetar_possibilidades()
            else :
                print("aceitou remocao parcial")
                print(qt_tentativas)
                solucao_inicial.copia(self.solucao_melhorada,janela_final)
                self.melhorou = True
                self.qt_visitados = 0
                self.roleta.atualizar_roleta(self.k)
                self.roleta.resetar_possibilidades()
                if self.solucao_melhorada.funcao_objetivo_tempo < solucao_inicial.funcao_objetivo_tempo:
                    qt_tentativas = 50
                else:
                    qt_tentativas -= 1                
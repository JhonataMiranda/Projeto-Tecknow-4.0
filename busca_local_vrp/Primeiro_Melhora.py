from env_vrp.Solucao import Solucao


class Primeiro_Melhora:

    def primeiro_melhora_swap_intra(self, solucao_inical, roteamento):
        s_linha = Solucao()
        janela_final = roteamento.colecao_clientes[0].janela_final
        # print("Fazendo Swap intra")
        for i in range(len(solucao_inical.vetor_solucao)):
            for j in range(1, len(solucao_inical.vetor_solucao[i].rota)):
                if len(solucao_inical.vetor_solucao[i].rota) == 1:
                    continue;
                for l in range(j+1, len(solucao_inical.vetor_solucao[i].rota)):
                    if len(solucao_inical.vetor_solucao[i].rota) == 1:
                        continue;
                    s_linha.copia(solucao_inical,janela_final)
                    conclui_mov = s_linha.swapIntra(i, j, l, roteamento)
                    if conclui_mov:
                        s_linha.calcula_funcao_objetivo_tempo(roteamento)
                        # print("Nova e Atual",s_linha.funcao_objetivo_tempo,solucao_inical.funcao_objetivo_tempo)
                        if s_linha.funcao_objetivo_tempo < solucao_inical.funcao_objetivo_tempo:
                            # print("Melhorou")
                            return s_linha
        # print("Não melhorou")
        return solucao_inical

    def primeiro_melhora_shift_intra(self, solucao_inical, roteamento):
        s_linha = Solucao()
        janela_final = roteamento.colecao_clientes[0].janela_final
        # print("Fazendo Shift intra")
        for i in range(len(solucao_inical.vetor_solucao)):
            for j in range(1, len(solucao_inical.vetor_solucao[i].rota)):
                for l in range(j+1, len(solucao_inical.vetor_solucao[i].rota)):

                    s_linha.copia(solucao_inical,janela_final)
                    conclui_mov = s_linha.shiftIntra(i, j, l, roteamento)
                    if conclui_mov:
                        s_linha.calcula_funcao_objetivo_tempo(roteamento)
                        # print("Nova e Atual",s_linha.funcao_objetivo_tempo,solucao_inical.funcao_objetivo_tempo)
                        if s_linha.funcao_objetivo_tempo < solucao_inical.funcao_objetivo_tempo:
                            # print("Melhorou")
                            return s_linha
        # print("Não melhorou")
        return solucao_inical

    def primeiro_melhora_swap_inter(self, solucao_inical, roteamento):
        s_linha = Solucao()
        janela_final = roteamento.colecao_clientes[0].janela_final
        # print("Fazendo Swap inter")
        for i in range(len(solucao_inical.vetor_solucao)-1):
            for j in range(len(solucao_inical.vetor_solucao[i].rota)):
                for k in range(i+1, len(solucao_inical.vetor_solucao)):
                    for l in range(len(solucao_inical.vetor_solucao[k].rota)):
                        s_linha.copia(solucao_inical,janela_final)
                        conclui_mov = s_linha.swapInter(i, j, k, l, roteamento)
                        if conclui_mov:
                            s_linha.calcula_funcao_objetivo_tempo(roteamento)
                            # print("Nova e Atual",s_linha.funcao_objetivo_tempo,solucao_inical.funcao_objetivo_tempo)
                            if s_linha.funcao_objetivo_tempo < solucao_inical.funcao_objetivo_tempo:
                                # print("Melhorou")
                                return s_linha
        # print("Não melhorou")
        return solucao_inical

    def primeiro_melhora_shift_inter(self, solucao_inical, roteamento):
        s_linha = Solucao()
        janela_final = roteamento.colecao_clientes[0].janela_final
        # print("Fazendo Shif Inter")
        for i in range(len(solucao_inical.vetor_solucao)-1):
            for j in range(len(solucao_inical.vetor_solucao[i].rota)):
                for k in range(i+1, len(solucao_inical.vetor_solucao)):
                    for l in range(len(solucao_inical.vetor_solucao[k].rota)):
                        s_linha.copia(solucao_inical,janela_final)
                        conclui_mov = s_linha.shiftInter(
                            i, j, k, l, roteamento)
                        if conclui_mov:
                            s_linha.calcula_funcao_objetivo_tempo(roteamento)
                            # print("Nova e Atual",s_linha.funcao_objetivo_tempo,solucao_inical.funcao_objetivo_tempo)
                            if s_linha.funcao_objetivo_tempo < solucao_inical.funcao_objetivo_tempo:
                                # print("Melhorou")
                                return s_linha
        # print("Não melhorou")
        return solucao_inical

    def primeiro_melhora_n_swap_inter(self, solucao_inical, roteamento):
        s_linha = Solucao()
        janela_final = roteamento.colecao_clientes[0].janela_final
        # print("Fazendo N Swap Inter")
        for i in range(len(solucao_inical.vetor_solucao)-1):
            for j in range(len(solucao_inical.vetor_solucao[i].rota)-1):
                for k in range(i+1, len(solucao_inical.vetor_solucao)):
                    for l in range(len(solucao_inical.vetor_solucao[k].rota)-1):
                        s_linha.copia(solucao_inical,janela_final)
                        conclui_mov = s_linha.nSwapInter(
                            2, i, j, k, l, roteamento)
                        if conclui_mov:
                            s_linha.calcula_funcao_objetivo_tempo(roteamento)
                            # print("Nova e Atual",s_linha.funcao_objetivo_tempo,solucao_inical.funcao_objetivo_tempo)
                            if s_linha.funcao_objetivo_tempo < solucao_inical.funcao_objetivo_tempo:
                                # print("Melhorou")
                                return s_linha
        # print("Não melhorou")
        return solucao_inical

    def primeiro_melhora_n_shift_inter(self, solucao_inical, roteamento):
        s_linha = Solucao()
        janela_final = roteamento.colecao_clientes[0].janela_final
        # print("Fazendo N Shift Inter")
        for i in range(len(solucao_inical.vetor_solucao)-1):
            for j in range(len(solucao_inical.vetor_solucao[i].rota)-1):
                for k in range(i+1, len(solucao_inical.vetor_solucao)):
                    for l in range(len(solucao_inical.vetor_solucao[k].rota)-1):
                        s_linha.copia(solucao_inical,janela_final)
                        conclui_mov = s_linha.nShiftInter(
                            2, i, j, k, l, roteamento)
                        if conclui_mov:
                            s_linha.calcula_funcao_objetivo_tempo(roteamento)
                            # print("Nova e Atual",s_linha.funcao_objetivo_tempo,solucao_inical.funcao_objetivo_tempo)
                            if s_linha.funcao_objetivo_tempo < solucao_inical.funcao_objetivo_tempo:
                                # print("Melhorou")
                                return s_linha
        # print("Não melhorou")
        return solucao_inical
    
    def primeiro_melhora_remove_menor_rota(self,solucao_inicial,roteamento):
        s_linha = Solucao()
        janela_final = roteamento.colecao_clientes[0].janela_final
        s_linha.copia(solucao_inicial,janela_final)
        conclui_mov = s_linha.eliminaMenorRota(roteamento)
        if conclui_mov:
            # s_linha.calcula_funcao_objetivo_tempo(roteamento)
            # if s_linha.funcao_objetivo_tempo < solucao_inicial.funcao_objetivo_tempo:
            return s_linha
        return solucao_inicial
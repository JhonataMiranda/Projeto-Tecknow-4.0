class Cliente:
    """
    Classe que representa um cliente 

    Atributos
    ----------
    id_cliente : int 
        representa o número de identificação de um cliente
    x : int
        coordenada x de um cliente
    y : int
        coordenada y de um cliente
    demanda : int
        quantidade de produtos que um cliente demanda
    janela_inicial : int
        tempo em minutos que se inicia a janela de tempo de um cliente
    janela_final : int
        tempo em minutos que se termina a janela de tempo de um cliente
    tempo_atendimento : int
        tempo que se gasta para atender um cliente
    custo_insercao : float
        custo de insercao de um cliente em uma rota
    
    Métodos
    -------
    copia()
        copia os valores de um cliente para outro
    exibe()
        mostra no terminal todos os dados de um cliente
    """
    def __init__(self, id, x, y, demanda, inicial, final, atendimento):
        """
        Parâmetros
        ----------
        id_cliente : int 
            representa o número de identificação de um cliente
        x : int
            coordenada x de um cliente
        y : int
            coordenada y de um cliente
        demanda : int
            quantidade de produtos que um cliente demanda
        janela_inicial : int
            tempo em minutos que se inicia a janela de tempo de um cliente
        janela_final : int
            tempo em minutos que se termina a janela de tempo de um cliente
        tempo_atendimento : int
            tempo que se gasta para atender um cliente
        custo_insercao : float
            custo de insercao de um cliente em uma rota
        """
        self.id_cliente = id
        self.x = x
        self.y = y
        self.demanda = demanda
        self.janela_inicial = inicial
        self.janela_final = final
        self.tempo_atendimento = atendimento
        self.custo_insercao = 0

    def copia(self):
        """Copia os atributos de um cliente para outro.

        Parâmetros
        ----------
        Nenhum

        Retorno
        ------
        cliente : Cliente
            Retorna um cliente com os dados copiados
        """
        cliente = Cliente()
        cliente.id_cliente = self.id_cliente
        cliente.demanda = self.demanda
        cliente.janela_inicial = self.janela_inicial
        cliente.janela_final = self.janela_final
        cliente.tempo_atendimento = self.tempo_atendimento
        cliente.custo_insercao = self.custo_insercao
        return cliente
    
    def exibe(self):
        """Exibe os dados do cliente no terminal.

        Parâmetros
        ----------
        Nenhum

        Retorno
        ------
        Nenhum
        """
        print("Id do cliente: ", self.id_cliente)
        print("Demanda do cliente: ", self.demanda)
        print("Janela de tempo inicial do cliente: ", self.janela_inicial)
        print("Janela de tempo final do cliente: ", self.janela_final)
        print("Tempo de atendimento: ", self.tempo_atendimento)
        print("Custo de inserção do cliente:", self.custo_insercao)
        print()

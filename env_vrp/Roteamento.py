from env_vrp.Cliente import Cliente


class Roteamento:
    """
    Classe que representa um problema de roteamento com seus dados 

    Atributos
    ----------
    numero_veiculos : int 
        representa a quantidade de veículos disponíveis
    numero_clientes : int
        representa a quantidade de clientes no problema
    capacidade_veiculos : int
        vetor que armazena a capacidade de cada um dos veículos
    colecao_clientes : Cliente
        vetor que armazena cada um dos clientes do problema
    matriz_custo_distancia : int
        uma matriz que armazena a distância do cliente i, representado pelo índice i, até o cliente j, representado pelo índice j
    matriz_custo_tempo : int
        uma matriz que armazena o tempo do cliente i, representado pelo índice i, ir até o cliente j, representado pelo índice j
    penalidade_veiculo : int
        penalidade de utilizar um veículo para construir uma rota

    Métodos
    -------
    ler_problema()
        le de um arquivo os dados do problema
    exibe()
        mostra no terminal todos os dados de um cliente

    """

    def __init__(self, path, isreal):
        """ Inicializa todas as variáveis da classe como 0 e os vetores como vazio
        Parâmetros
        ----------
        path: string
            caminho que deve ser percorrido no sistema de arquivos da maquina para
            encontrar o arquivo com os dados do problema
        """
        self.numero_veiculos = 0
        self.numero_clientes = 0
        self.capacidade_veiculos = []
        self.colecao_clientes = []
        self.matriz_custo_distancia = []
        self.matriz_custo_tempo = []
        self.penalidade_veiculo = 1000
        if isreal:
            self.ler_problema_real(path)
        else:
            self.ler_problema(path)

    def ler_problema(self, path):
        """ Lê do arquivo recebido os dados necessários para construir e resolver
        um problema de roteamento de veículos. Também define todas os atributos.
        Parâmetros
        ----------
        path: string
            caminho que deve ser percorrido no sistema de arquivos da maquina para
            encontrar o arquivo com os dados do problema
        Retorno
        ------
        Nenhum
        """
        instancia = open(path, 'r')
        texto = []
        for linha in instancia:
            texto.append(linha.split())

        # define numero de clientes e numero de veiculos
        self.numero_clientes = int(texto[0][0])
        self.numero_veiculos = int(texto[0][2])
        # preenche a capacidade dos veiculos
        self.capacidade_veiculos = [int(texto[0][1])
                                    for x in range(self.numero_veiculos)]
        # le os dados dos clientes
        for linha in range(3, self.numero_clientes+4):
            id = int(texto[linha][0])
            x = int(texto[linha][1])
            y = int(texto[linha][2])
            demanda = int(texto[linha][3])
            janela_inicial = int(texto[linha][4])
            janela_final = int(texto[linha][5])
            tempo_atendimento = int(texto[linha][6])
            cliente = Cliente(id, x, y, demanda, janela_inicial,
                              janela_final, tempo_atendimento)
            self.colecao_clientes.append(cliente)
        # le matriz de custo
        for linha in range(self.numero_clientes+5, len(texto)):
            for item in range(0, len(texto[linha])):
                texto[linha][item] = float(texto[linha][item])
            self.matriz_custo_tempo.append(texto[linha])
            self.matriz_custo_distancia.append(texto[linha])

    def ler_problema_real(self, path):
        """ Lê do arquivo de instancia real recebido os dados necessários para construir e resolver
        um problema de roteamento de veículos. Também define todas os atributos.

        Parâmetros
        ----------
        path: string
            caminho que deve ser percorrido no sistema de arquivos da maquina para
            encontrar o arquivo com os dados do problema

        Retorno
        ------
        Nenhum
        """
        instancia = open(path, 'r')
        texto = []
        for linha in instancia:
            texto.append(linha.split())

        # define numero de clientes e numero de veiculos
        self.numero_clientes = int(texto[0][0])
        self.numero_veiculos = int(texto[0][2])
        # preenche a capacidade dos veiculos
        self.capacidade_veiculos = [int(texto[0][1])
                                    for x in range(self.numero_veiculos)]
        # le os dados dos clientes
        for linha in range(3, self.numero_clientes+4):
            id = int(texto[linha][0])
            x = 0
            y = 0
            if id != 0:
                if texto[linha][1] == '-':
                    demanda = 2
                else:
                    demanda = int(texto[linha][1])
                if texto[linha][2] == '-':
                    janela_inicial = 0
                else:
                    janela_inicial = int(texto[linha][2])
                if texto[linha][3] == '-':
                    janela_final = 370
                else:
                    janela_final = int(texto[linha][3])
                if texto[linha][4] == '-':
                    tempo_atendimento = 5
                else:
                    tempo_atendimento = int(texto[linha][4])
            else:
                demanda = 0
                janela_inicial = 0
                # TODO VERIFICAR QUAL A JANELA FINAL
                janela_final = 370
                tempo_atendimento = 0
            cliente = Cliente(id=id, x=x, y=y, demanda=demanda, inicial=janela_inicial,
                              final=janela_final, atendimento=tempo_atendimento)
            self.colecao_clientes.append(cliente)
        # le matriz de custo
        inicio_matriz_custo = self.numero_clientes+5
        fim_matriz_custo = inicio_matriz_custo + self.numero_clientes
        for i in range(inicio_matriz_custo, fim_matriz_custo+1):
            linha = texto[i][0].split()
            linha = linha[0].split(",")
            linha = [(int(element)/60) for element in linha if element != ""]
            self.matriz_custo_tempo.append(linha)
        # pula mais uma linha para tirar o texto que delimita as matrizes
        inicio_matriz_distancia = fim_matriz_custo+2
        fim_matriz_distancia = inicio_matriz_distancia + self.numero_clientes
        for i in range(inicio_matriz_distancia, fim_matriz_distancia+1):
            linha = texto[i][0].split()
            linha = linha[0].split(",")
            linha = [int(element) for element in linha if element != ""]
            self.matriz_custo_distancia.append(linha)

    def exibe(self):
        """Exibe os dados do problema de roteamento no terminal.

        Parâmetros
        ----------
        Nenhum

        Retorno
        ------
        Nenhum
        """
        print("Número de veículos:", self.numero_veiculos)
        print("Número de clientes:", self.numero_clientes)
        for id_veiculo in range(len(self.capacidade_veiculos)):
            print("Capacidade do veículo ", id_veiculo + 1,
                  ":", self.capacidade_veiculos[id_veiculo])
        for cliente in self.colecao_clientes:
            cliente.exibe()
            print()
        print("###################################################################################")
        print("Matriz de custo de tempo:")
        for linha in self.matriz_custo_tempo:
            print(linha)
        print("###################################################################################")
        print("Matriz de custo de distância:")
        for linha in self.matriz_custo_distancia:
            print(linha)
        print("Penalidade de inserir um veículo:", self.penalidade_veiculo)

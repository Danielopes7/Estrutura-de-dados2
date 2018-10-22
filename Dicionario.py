class CarregaPalavras:

    def __init__(self, Dicionario, id_doc):
        self.Dicionario = Dicionario
        self.id_doc = id_doc


    def GetQtd(self):
        return self.Dicionario

    def Get_ID(self):
        return self.id_doc

    def Incremento(self):
        self.qtd = self.qtd + 1


class ContaOcorrencias:

    def __init__(self, string):
        self.string = string
        self.ocorrencias = 0

    def Ocorrencias(self, palavra):
        ocorre = self.string.count(palavra)
        return ocorre




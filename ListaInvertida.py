class IndiceInvertido:
    def __init__(self,id_doc,palavra,qtd):
        self.id_doc=id_doc
        self.qtd=qtd
        self.palavra=palavra


    def getId_Doc(self):
        return self.id_doc

    def getQtd(self):
        return self.qtd

    def getPalavra(self):
        return self.palavra

class IndiceInvertidoTotal:
    def __init__(self,palavra):
        self.id_doc=[]
        self.qtd=[]
        self.palavra=palavra


    def getId_Doc(self):
        return self.id_doc[0]

    def getQtd(self):
        return self.qtd

    def getPalavra(self):
        return self.palavra

    def setID(self,doc):
        self.id_doc.append(doc)


    def setQtd(self,qtd):
        self.qtd.append(qtd)




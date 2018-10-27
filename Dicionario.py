from Hashing import FazerChave


class Dicionario:

    def __init__(self, tam, C, opcao):
        self.Tabela = [[False, None, None] for i in range(tam)]
        self.tam = tam
        self.C = C
        self.opcao = opcao

    def __str__(self):
        string = '\n'
        for i in self.Tabela:
            if i[0]:
                string += i[1] + " : " + str(i[2]) + '\n'

        return string

    def Insert(self, palavra, data):
        iteracao = 0
        key = FazerChave(palavra, self.C)
        h = (key + iteracao) % self.tam

        # -----------------------TRATAR COLISAO DE MODO LINEAR--------------------
        if self.opcao == 'linear':

            while self.Tabela[h][0] == True and iteracao < self.tam:
                iteracao = iteracao + 1
                h = (key + iteracao) % self.tam

            if iteracao < self.tam:
                self.Tabela[h][0] = True
                self.Tabela[h][1] = palavra
                self.Tabela[h][2] = data

            else:
                print("\nTabela Hashing Lotada\n")
        # -----------------------TRATAR COLISAO DE MODO QUADRATICO-----------------
        VerificaLotacao = 0
        if self.opcao == 'quadratica':

            for i in self.Tabela:  # verifico se a tabela ta lotada
                if i[0] == True:
                    VerificaLotacao += 1

            while self.Tabela[h][0] == True and VerificaLotacao < self.tam:
                iteracao = iteracao + 1
                h = (h + iteracao) % self.tam
                print("a")
            if VerificaLotacao < self.tam:
                self.Tabela[h][0] = True
                self.Tabela[h][1] = palavra
                self.Tabela[h][2] = data

            else:
                print("\nTabela Hashing Lotada\n")

    def Query(self, palavra):
        key = FazerChave(palavra, self.C)
        iteracao = 0
        h = (key + iteracao) % self.tam

        # ------------------BUSCA OPCAO LINEAR-------------------------------------
        if self.opcao == 'linear':

            while self.Tabela[h][1] != palavra and iteracao < self.tam:
                iteracao = iteracao + 1
                h = (key + iteracao) % self.tam

            if iteracao < self.tam:
                return self.Tabela[h][2]

            else:
                return -1
        # ------------------BUSCA OPCAO QUADRATICA---------------------------------
        ocorre=0
        if self.opcao == 'quadratica':
            for i in self.Tabela:
                if i[1]== palavra:
                    ocorre+=1
            if ocorre>0:

                while self.Tabela[h][1] != palavra:

                    iteracao = iteracao + 1
                    h = (h + iteracao) % self.tam

                return self.Tabela[h][2]

            else:

                return -1

from ListaInvertida import IndiceInvertido


def OpenFile(doc):
    file = open(doc, 'r')

    String = file.read()  # pegando o texto do arquivo e botando na string
    String = Minusculo(String)

    return String


def Minusculo(string):  # deixa todas as letras que estavam maiuscula em minuscula
    minusculo = string.lower()

    return minusculo


def CriaDicionario(string, C):
    ListaDePalavras = string.split()  # crio uma lista com todas as palavras do arquivo
    ListaDePalavras = sorted(ListaDePalavras)  # mantenho a lista em ordem alfabetica como um dicionario
    b = '!@#$%¨¨&*()-=.,><>:^}~][´{|?/'  # caracteres que nao sao validos como palavra
    Dicionario = {}

    for palavra in ListaDePalavras:  # percorro a lista de palavras
        tam = int(len(palavra))  # tamanho de cada palavra
        if tam >= C:  # se o tamanho da palavra for maior que a variavel C que será recebida podemos adicionar no dicionario

            for i in range(0, len(b)):  # nesse for removo os caracteres invalido de uma palavra
                palavra = palavra.replace(b[i], "")
            value = string.count(palavra)  # quantidade de vezes que a palavra aparece no arquivo
            key = palavra  # a key do dicionario vai ser a palavra
            Dicionario[key] = value
            print(" dicio : {}".format(Dicionario))

    return Dicionario


def CriaIndex(NomeDoc, Dicionario):
    palavras = []
    for k, v in Dicionario[NomeDoc].items():
        palavras.append(IndiceInvertido(NomeDoc, k, v))

    return palavras

def CriaListaInvertida(palavras,Dicionario):

    for palavra in palavras:
        for i in range (i ,len(palavras))
            if
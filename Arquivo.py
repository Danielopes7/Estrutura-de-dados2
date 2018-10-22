from ListaInvertida import IndiceInvertido
from ListaInvertida import IndiceInvertidoTotal
import os.path
import sys
import operator

def OpenFile(doc):
    existe = os.path.exists(doc)  # antes de usar a função é preciso saber se o arquivo existe
    if existe:
        file = open(doc, 'r')

        String = file.read()  # pegando o texto do arquivo e botando na string
        String = Minusculo(String)
        print("\nTEXTO IFORMADO PELO USUÁRIO:\n\n{}\n".format(String))
        return String
    else:
        print("\nO arquivo:[{}] não existe tente novamente.".format(
            doc))  # se o arquivo nao existe o programa é finalizado
        sys.exit()


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
    for i in range(0, len(NomeDoc)):
        for k, v in Dicionario[NomeDoc[i]].items():
            palavras.append(IndiceInvertido(i+1, k, v))
    palavras=sorted(palavras,key=operator.attrgetter('palavra'))
    return palavras


def CriaListaInvertidaa(palavras):
    ListaInvertida = []
    palavrasJaUsadas = []
    KeyList = 0
    for i in range(0, len(palavras)):
        if (palavrasJaUsadas.count(palavras[i].getPalavra()) == 0):

            ListaInvertida.append(IndiceInvertidoTotal(palavras[i].getPalavra()))
            ListaInvertida[KeyList].setID(palavras[i].getId_Doc)
            ListaInvertida[KeyList].setQtd(palavras[i].getQtd)

            for j in range(i + 1, (len(palavras))):

                if (palavras[i].getPalavra() == palavras[j].getPalavra()):
                    ListaInvertida[KeyList].setID(palavras[j].getId_Doc)
                    ListaInvertida[KeyList].setQtd(palavras[j].getQtd)

            KeyList = KeyList + 1
            palavrasJaUsadas.append(palavras[i].getPalavra())

    return ListaInvertida

def Quantidade_Documento(palavra):
    Lista=[]
    Lista_id_qtd = []
    Lista.append(palavra)

def CriaListaInvertida(palavras):
    ListaPalavra = []
    Lista_id_qtd = []
    palavrasJaUsadas = []
    ListaInvertida=[]
    tamLista=0
    l = 0
    r = 2
    for i in range(0, len(palavras)):
        if (palavrasJaUsadas.count(palavras[i].getPalavra()) == 0):

            ListaPalavra.append(palavras[i].getPalavra())
            Lista_id_qtd.append(palavras[i].getQtd())
            Lista_id_qtd.append(palavras[i].getId_Doc())
            ListaPalavra.append(Lista_id_qtd[l:r])
            l = l + 2
            r = r + 2

            for j in range(i + 1, (len(palavras))):

                if (palavras[i].getPalavra() == palavras[j].getPalavra()):
                    Lista_id_qtd.append(palavras[j].getQtd())
                    Lista_id_qtd.append(palavras[j].getId_Doc())
                    ListaPalavra.append(Lista_id_qtd[l:r])
                    l = l + 2
                    r = r + 2
            ListaPalavra[tamLista+1:]=sorted(ListaPalavra[tamLista+1:],reverse=True)

            ListaInvertida.append(ListaPalavra[tamLista:])
            tamLista=len(ListaPalavra)
            palavrasJaUsadas.append(palavras[i].getPalavra())

    print("tamanho de palavras{}".format(len(palavrasJaUsadas)))

    return ListaInvertida
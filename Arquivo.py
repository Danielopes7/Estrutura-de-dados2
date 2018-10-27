from ListaInvertida import IndiceInvertido

import os.path
import sys
import operator


def OpenFile(doc, contador):
    existe = os.path.exists(doc)  # antes de usar a função é preciso saber se o arquivo existe
    if existe:
        file = open(doc, 'r')

        String = file.read()  # pegando o texto do arquivo e botando na string
        String = Minusculo(String)
        print("\nTEXTO IFORMADO PELO USUÁRIO [ ID={}]:\n\n{}\n".format(contador, String))
        return String
    else:
        print("\nO arquivo:[{}] não existe tente novamente.".format(
            doc))  # se o arquivo nao existe o programa é finalizado
        sys.exit()


def Minusculo(string):  # deixa todas as letras que estavam maiuscula em minuscula
    minusculo = string.lower()

    return minusculo


def CriaDict(string, C):
    ListaDePalavras = string.split()  # crio uma lista com todas as palavras do arquivo
    ListaDePalavras = sorted(ListaDePalavras)  # mantenho a lista em ordem alfabetica como um dicionario
    b = '!@#$%¨¨&*()-=.,><>:^}~][´{|?/'  # caracteres que nao sao validos como palavra
    Dicionario = {}
    j = 0

    for i in ListaDePalavras: #removo os caracteres invalidos da lista toda
        for i in range(0, len(b)):  # nesse for removo os caracteres invalido de uma palavra da lista
            ListaDePalavras[j] = ListaDePalavras[j].replace(b[i], "")
        j = j + 1

    for palavra in ListaDePalavras:  # percorro a lista de palavras
        tam = int(len(palavra))  # tamanho de cada palavra
        if tam >= C:  # se o tamanho da palavra for maior que a variavel C que será recebida podemos adicionar no dicionario

            value = ListaDePalavras.count(palavra)  # quantidade de vezes que a palavra aparece na Lista
            key = palavra  # a key do dicionario vai ser a palavra
            Dicionario[key] = value


    return Dicionario


def CriaIndex(NomeDoc, Dicionario):
    palavras = []
    for i in range(0, len(NomeDoc)):
        for k, v in Dicionario[NomeDoc[i]].items():
            palavras.append(IndiceInvertido(i + 1, k, v))
    palavras = sorted(palavras, key=operator.attrgetter('palavra'))
    return palavras


def CriaListaInvertida(palavras):
    ListaPalavra = []
    Lista_id_qtd = []
    palavrasJaUsadas = []
    ListaInvertida = []
    tamLista = 0
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
            ListaPalavra[tamLista + 1:] = sorted(ListaPalavra[tamLista + 1:], reverse=True)

            ListaInvertida.append(ListaPalavra[tamLista:])
            tamLista = len(ListaPalavra)
            palavrasJaUsadas.append(palavras[i].getPalavra())



    return ListaInvertida

def QtdTermosDiferentes(Nome_Documento,Dict):
    QtdPalavrasDiferentes = []

    for i in range(0, len(Nome_Documento)):
        QtdPalavrasDiferentes.append(len(Dict[Nome_Documento[i]]))

    return QtdPalavrasDiferentes
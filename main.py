import Arquivo as arq
from ListaInvertida import IndiceInvertido
from Dicionario import ContaOcorrencias

flag = 0
Nome_Documento = []
string = []
Dicionario = {}

while (flag == 0):  # primeiro passo do programa é pedir ao usuário para inserir os arquivos
    # uso um estilo switch para obter um menu que o usuário insira quantos arquivos quiser
    comando = int(input("ADICIONAR ARQUIVO[1]\n PARAR DE ADICIONAR[2]"))

    if comando == 1:
        Nome_Documento.append(str(input("qual o nome do arquivo?")))  # exemplo de entrada = doc1.txt
    elif comando == 2:
        flag = 1

for NomeArq in Nome_Documento:  # percorre a Lista Nome_Documento
    string.append(arq.OpenFile(NomeArq))  # le todos os documentos recebidos e joga em uma lista chamada string

C = int(input("Qual o valor de C"))  # valor da Variavel C

for i in range(0, len(string)):
    Dicionario[Nome_Documento[i]] = arq.CriaDicionario(string[i],C)  # o arq.Criadicionario é responsavel por criar um dicionario que vai ser atribuido a outro dicionario {'Nome_Documento':{'palavra':Ocorrencias}}
                                                                     # ou seja nesse Dicionario eu possuo todos os elementos que preciso para o Indice Invertido (id_doc,quantidade,palavra)
for i in range(0, len(Nome_Documento)):
    palavras = arq.CriaIndex(Nome_Documento[i], Dicionario)  #uso o CriaIndex para criar uma lista de objetos(palavras) da classe ListaInvertida, com essa lista de objetos possuo meio que um Indice Invertido de cada documento


for i in range (0,len(palavras)):
    print('{} {} {}'.format(palavras[i].getPalavra(),palavras[i].getQtd(),palavras[i].getId_Doc()[:-4]))




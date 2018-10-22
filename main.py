import Arquivo as arq
import sys
from ListaInvertida import IndiceInvertido
from Dicionario import ContaOcorrencias

flag = 0
Nome_Documento = []
string = []
Dicionario = {}

while (flag == 0):  # primeiro passo do programa é pedir ao usuário para inserir os arquivos
    # uso um estilo switch para obter um menu que o usuário insira quantos arquivos quiser
    comando = int(input("\nAdicionar Arquivo[1]\nPara de Adicionar[2]\n="))

    if comando == 1:
        Nome_Documento.append(str(input("\nQual o nome do arquivo?\n=")))  # exemplo de entrada = doc1.txt
    elif comando == 2:
        flag = 1
    elif comando!=2 and comando!=1:
        print("\nDigite Novamente.\n")

if len(Nome_Documento) == 0:  # caso o usuário nao insira nenhum arquivo
    sys.exit()  # sair do programa

for NomeArq in Nome_Documento:  # percorre a Lista Nome_Documento
    string.append(arq.OpenFile(NomeArq))  # le todos os documentos recebidos e joga em uma lista chamada string

C = int(input("Qual o valor de C"))  # valor da Variavel C

for i in range(0, len(string)):
    Dicionario[Nome_Documento[i]] = arq.CriaDicionario(string[i],
                                                       C)  # o arq.Criadicionario é responsavel por criar um dicionario que vai ser atribuido a outro dicionario {'Nome_Documento':{'palavra':Ocorrencias}}

    # ou seja nesse Dicionario eu possuo todos os elementos que preciso para o Indice Invertido (id_doc,quantidade,palavra)

AllWords = (arq.CriaIndex(Nome_Documento,Dicionario))  # uso o CriaIndex para criar uma lista de objetos(palavras) da classe ListaInvertida, com essa lista de objetos possuo meio que um Indice Invertido de cada documento


for i in range(0, len(AllWords)):
    print('{} {} {}'.format(AllWords[i].getPalavra(), AllWords[i].getQtd(), AllWords[i].getId_Doc()))

IndexInverted=arq.CriaListaInvertida(AllWords)

print("\n[Indice Invertido]:")
for percorre in IndexInverted:
    print(percorre[0],end='')
    j=0
    for i in range(1,len(percorre)):
        print(" {} {} ".format(percorre[i][j],percorre[i][j+1]),end='')
    print("")


import Arquivo as arq
import sys
from Dicionario import Dicionario
from IDF import IDF
flag = 0
Nome_Documento = []
string = []
Dict = {}
contador=1
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

    string.append(arq.OpenFile(NomeArq,contador))  # le todos os documentos recebidos e joga em uma lista chamada string
    contador=contador+1
C = int(input("Qual o valor de C"))  # valor da Variavel C

if C==0:
    print("\nComo o valor mínimo que ser pode assumir é 1, então o C=0 será transformado para C=1\n")
    C=1

for i in range(0, len(string)):
    Dict[Nome_Documento[i]] = arq.CriaDict(string[i],C)  # o arq.Criadicionario é responsavel por criar um dicionario que vai ser atribuido a outro dicionario {'Nome_Documento':{'palavra':Ocorrencias}}

    # ou seja nesse Dicionario eu possuo todos os elementos que preciso para o Indice Invertido (id_doc,quantidade,palavra)



AllWords = (arq.CriaIndex(Nome_Documento,Dict))  # uso o CriaIndex para criar uma lista de objetos(palavras) da classe ListaInvertida, com essa lista de objetos possuo meio que um Indice Invertido de cada documento
for i in range(0,len(AllWords)):
    print(AllWords[i].getPalavra())


IndexInverted=arq.CriaListaInvertida(AllWords)
print(IndexInverted)
print("\n[Indice Invertido]:")
for percorre in IndexInverted:
    print(percorre[0],end='')
    j=0
    for i in range(1,len(percorre)):
        print(" {} {} ".format(percorre[i][j],percorre[i][j+1]),end='')
    print("")

#-------------------- escolhendo qual metodo irá tratar as colisões-------------#

comando = int(input("\nQual o método para tratar as colisões?\nLinear [1]\nQuadratica[2]\nArvore Rubro Negra[3]"))

if comando==1:
    TAD = Dicionario(len(IndexInverted), C, 'linear')

elif comando==2:
    TAD = Dicionario(len(IndexInverted), C, 'quadratica')

for percorre in IndexInverted:
    TAD.Insert(percorre[0],percorre)

print(TAD)
x=TAD.Query('animal')
print(x[1][1])
#------ MENU DA BUSCA -----------------------------------------------------------------------------------#

TermosDiferentes=arq.QtdTermosDiferentes(Nome_Documento,Dict) #cria uma lista com os termos diferentes de cada documento que vai ser usado para implementar o IDF


Menu=True
while Menu==True:
    comando = int(input("\nProcurar nos Documentos [1]\nParar de Procurar[2]\n="))
    if comando==1:
        text=(input("\n Procurar o Texto:"))
        IDF(text,TAD,TermosDiferentes,len(Nome_Documento))
    if comando==2:
        Menu=False

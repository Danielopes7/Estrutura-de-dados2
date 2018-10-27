import math
def IDF(busca,TAD,ListaTermos,Num_Docs):
    print("busca= {}  TAD={} LISTATERMOS={}  NUM DE DOCS={}".format(busca,TAD,ListaTermos,Num_Docs))
    palavras=busca.split()
    IDF=[]
    IDF_total=[]
    l=0
    r=2
    documentos=[]       # crio uma lista dizendo quais documentos tem as palavras da busca
    for i in palavras:
        x=TAD.Query(i)
        if x==-1:
            print("\nNão foi encontrada a palavra = {}\n".format(i))
            return 0
        print("tamanho de x{}".format(len(x)))
        for j in range(1,len(x)):
            x[j][1]

            if documentos.count(x[j][1])==0:
                documentos.append(x[j][1])

    print("lista de documentos :{}".format(documentos))


    for i in documentos:
        print("valor do i:{}".format(i))
        idf=0
        for j in range (0,len(palavras)):
            y=TAD.Query(palavras[j])
            print("lista que contem a palavra{}".format(y))
            Dj=len(y)-1
            print("Dj:{}".format(Dj))
            freq=frequencia(y,i)
            print("frequencia : {}".format(freq))
            idf+=freq*(math.log(Num_Docs,2)/Dj)

        print("valor do idf antes:{}".format(idf))
        idf=idf/ListaTermos[i-1]
        print("valor do idf depois{}".format(idf))
        IDF.append(idf)
        IDF.append(i)
        IDF_total.append(IDF[l:r])
        l = l + 2
        r = r + 2
    print(sorted(IDF_total,reverse=True))

def frequencia(lista,documento):
    lista=lista[1:]
    for i in lista:
        if i[1]==documento:
            return i[0]
    return 0







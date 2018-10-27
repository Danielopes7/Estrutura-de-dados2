def FazerChave(palavra,C):
    chave=0
    Primeiros_C=palavra[:C]

    for i in range(0,len(Primeiros_C)):
            chave+=ord(Primeiros_C[i])


    return chave



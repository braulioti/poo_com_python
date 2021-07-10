def tupla_par(tupla):
    i = 0
    resposta = []
    while (i < len(tupla)):
        if (i % 2 == 0):
            resposta.append(tupla[i])
        i = i + 1
    return resposta

print(tupla_par(['oi', 'estou', 'estudando', 'poo']))
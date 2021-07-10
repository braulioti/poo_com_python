def numero_perfeito(num):
    i = num
    soma = 0
    resposta = ''
    while (i > 1):
        i = i - 1
        if (num % i == 0):
            soma = soma + i
            if (resposta == ''):
                resposta = str(i)
            else:
                resposta = resposta + ' + ' + str(i)
            resposta = resposta.format(i)

        if (i == 1):
            resposta = resposta + ' = ' + str(soma)
            if (soma == num):
                resposta = resposta + ' (perfeito)'
            else:
                resposta = resposta + ' (imperfeito)'
    return resposta

print(numero_perfeito(28))
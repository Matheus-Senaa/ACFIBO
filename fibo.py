anterior = 0
proxima = 1
soma = 1

for n in range (0, 101):
    print(anterior)
    soma = proxima + anterior
    anterior = proxima
    proxima = soma

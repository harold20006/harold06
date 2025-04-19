numeros = [2,4,6,8,10,12,14,16,18,20];

def suma(numeros):
    suma=0
    for i in range(len(numeros)):
        suma += numeros[i]
    return suma
def media(numeros):
    suma=0
    for i in range(len(numeros)):
        suma += numeros[i]
    media = suma/len(numeros)
    return media
def maximo(numeros):
    maximo = numeros[0]
    for i in range(len(numeros)):
        if numeros[i] > maximo:
            maximo = numeros[i]
    return maximo
def minimo(numeros):
    minimo = numeros[0]
    for i in range(len(numeros)):
        if numeros[i] < minimo:
            minimo = numeros[i]
    return minimo
def varianza(numeros):
    suma=0
    for i in range(len(numeros)):
        suma += numeros[i]
    media = suma/len(numeros)
    varianza = 0
    for i in range(len(numeros)):
        varianza += (numeros[i]-media)**2
    varianza = varianza/len(numeros)
    return varianza
print('-='*23)
print('{:^23}'.format('SORTEANDO E SOMANDO VALORES PARES'))
print('-='*23)
from random import randint
from time import sleep

def sorteia(lista):
    print('SORTEANDO 5 VALORES DA LISTA: ',end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ',end='', flush=True)
        sleep(1)
    print('PRONTO')

def somaPAR(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valore da {lista}, temos {soma} com Soma pares ')

#PROGRAMA PRINCIPAL
numeros = list()
sorteia(numeros)
somaPAR(numeros)                 



    
def mostralinha():
    print('-'*35)
mostralinha()
print('{:^35}'.format(' ACHAR O MAIOR VALOR ENTRE OS PARÃMETROS'))
from time import sleep

def maior(*num):
    print('-'*35)
    print('Analisando os valores passados...')
    sleep(1)
    cont = 0
    for c in num:
        cont += 1
    if cont > 0:
        m = max(num)
    else:
        m = 0
    print(f'{num} Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {m}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

def mostralinha():
    print('-'*35)
    print('   CONTADOR 3   ')
    print(''*35)

from time import sleep

def maior(* num):
    print('-'*35)
    cont = 0
    for v in num:
         cont += 1
    print('Analizando os valores passados...')
    sleep(1)
    print(f'{num} foram informados {cont} valores ao todo. ')
    print(f'O maior valor informado foi {max(num)}')

maior(2, 1, 8, 4)
maior(3, 5, 1)

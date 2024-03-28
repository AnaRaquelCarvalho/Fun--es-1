def mostralinha():
    print('-'*35)
    print('   CONTADOR    ')
    print('-'*35)
print('')
from time import sleep

def contador(i, f, p ):
    if p < 0:
        p== -1
    if p == 0:
        p = 1
    print('-'*35) 
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end= '', flush=True)
            sleep(1.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='', flush=True)
            sleep(1)
            cont -= p
        print('FIM !')

#PROGRAMA PRINCIPAL
contador(1,10,1)   
contador(10, 0, 2)
contador(2,10,2) 
contador(0,100,10)
print('-'*35)
print('Agora é a sua vez de personalizar a contagem! ')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)

def mostralinha():
    print('-'*40)
mostralinha()
print('{:^40}'.format('  CÁLCULOS DA ÁREA DE TERRENOS '))    
mostralinha()

def terreno(largura,comprimento):
    soma = largura * comprimento
    mostralinha()
    print('{:^40}'.format(' RESULTADO DO CÁLCULO: '))
    print(f'A área de um terreno de {largura} x {comprimento} é de {soma} m².') 

#PROGRAMA PRINCIPAL
largura = float(input('Largura(m):  '))
comprimento = float(input('Comprimento(m): '))
terreno(largura, comprimento)
mostralinha()    

            
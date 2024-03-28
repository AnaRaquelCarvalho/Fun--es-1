def mostralinha():
    print('-'*36)
mostralinha()    
print('     SISTEMA DE MENSAGENS AUTOMÁTIZADAS   ')
mostralinha()

def titulo(texto):
    print('~'*len(texto)*2)
    print(texto.center(len(texto)*2,' '))
    print('~'*len(texto)*2)

#PROGRAMA PRINCIPAL
msg = str.title(input('Informe uma mensagem: '))
titulo(msg)
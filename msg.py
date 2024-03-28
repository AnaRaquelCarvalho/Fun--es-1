def mostralinha():
    print('-'*36)
mostralinha()    
print('     SISTEMA DE MENSAGENS 2    ')
mostralinha()

def Escreva(palavra):
    tamanho = len(palavra)+2
    print("-"*(tamanho))
    print(f'  {palavra.center(tamanho)}')
    print("-"*(tamanho))

palavra = input("Digite qualquer palavra: ")
print(Escreva(palavra=palavra))
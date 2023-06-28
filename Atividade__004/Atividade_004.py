palavras_digitadas = []


for _ in range(0, 5):
    palavras = str(input('Digite alguma palavra: '))
    
    if palavras.isalpha() == False:
        print('\033[0;31mERROR: digite apenas letras.\033[0m')
        continue
    
    palavras_digitadas.append(palavras)

contador_de_vogais = 0

for palavra in palavras_digitadas:
    print(f'\nA palavra: [{palavra}] tem as seguintes vogais:', end=' ')
    
    for letra in palavra:
        if letra in 'AeiouaeiouAEIOU':
            print( f'[{letra}]', end='')

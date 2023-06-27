palavras_digitadas = []
palavras_selecionadas = []
    

def letras(lista):

    for palavras in lista:
        if (len(palavras) > 3) and (palavras[0] in ('A')):
            palavras_selecionadas.append(palavras)

    print(f'As palavras digitadas pelo úsuario que começam com a letra "A" e tem mais de 3 letras foram: {palavras_selecionadas}')


while True:
    palavras = str(input('Digite qualquer palavra: ')).upper().lstrip().rstrip()
    
    while (palavras.isalpha() == False):
        print('\033[0;31mERROR: Digite somente letras.\033[0m')
        palavras = str(input('Digite qualquer palavra: ')).upper().lstrip().rstrip()
 
    palavras_digitadas.append(palavras)

    continuar = str(input('Continuar?[S/N] '))

    while (continuar not in 'SsnN'):
        print('\033[0;31mERROR: Digite a opção correta..\033[0m')
        palavras = str(input('Digite qualquer palavra: ')).upper().lstrip().rstrip()
    
    if continuar in 'nN':
         break
    
letras(palavras_digitadas)



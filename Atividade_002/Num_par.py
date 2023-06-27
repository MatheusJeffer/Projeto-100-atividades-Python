numeros_digitados = []



def num_par(numeros):
    numeros_pares = []

    for numero in numeros:
        if numero %2 == 0:
           numeros_pares.append(numero)

    media_total_dos_pares = sum(numeros_pares) / len(numeros_pares)    

    print(f'A média total dos números pares é: [{media_total_dos_pares}]')


continuar = ''

while continuar in 'Ss':
    numeros = str(input('Digite algum número: '))
    
    while numeros.isnumeric() == False:
        print('\033[0;31mERROR: Digite um valor númerico.\033[0m')
        numeros = str(input('Digite algum número: '))

    numeros_int = int(numeros)
    numeros_digitados.append(numeros_int)

    continuar = str(input('Continuar?[S/N] '))
    
    while continuar not in 'sSnN':
         print('\033[0;31mERROR: Digite uma opção válida.\033[0m')
         continuar = str(input('Continuar?[S/N] '))
        
num_par(numeros_digitados)


def invert(txt):
  palavra = txt
  quant = len(palavra)

  while  quant > 0:
    quant -= 1
    print(palavra[quant], end='')  
        

texto = str(input('Digite algo: '))

invert(texto)
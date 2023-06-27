def invert(txt):
   if txt  not in 'Nada':
     return txt[::-1]
   else:
      return 'Nada digitado.'

Str = str(input('Digite alguma palavra: ')) or 'Nada'

print(invert(Str))
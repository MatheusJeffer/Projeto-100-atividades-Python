def invert(txt):
   string_invertida = str(txt)
   return string_invertida[::-1]

Str = str(input('Digite alguma palavra: '))

print(invert(Str))
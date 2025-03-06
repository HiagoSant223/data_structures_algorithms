a = 'casaco'

print(a)

maiuscula = a.upper()
print(maiuscula)

minuscula = a.lower()
print(minuscula)

capital = a.capitalize()
print(capital)

metadePalavra = a[0:3]
print(metadePalavra)

ultimas_letras = a[3:]
print(ultimas_letras)

b = a.replace('aco', 'inha')
print(b)

c = a.replace('o', 'a')
print(c)

print(c.find('a'))

e = ' casaco '

print(len(e))

f = e.strip()
print(len(f))

n1 = 14
n2 = 16

print(f'Dividindo {n1} por {n2} p resultado e {n1/n2}')
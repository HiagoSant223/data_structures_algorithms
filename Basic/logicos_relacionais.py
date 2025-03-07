"""
Operadores Lógicos

Operador    Descrição                           Exemplo    Resultado
and         Retorna True se ambos
            os operandos forem verdadeiros      True and False    False

or          Retorna True se pelo menos um dos   True or False    True
            operandos for verdadeiro            
not         Inverte o valor lógico do operando  not True    False

Operadores Relacionais

Operador    Descrição    Exemplo    Resultado
==    Igual a    5 == 5    True
!=    Diferente de    5 != 3    True
>    Maior que    5 > 3    True
<    Menor que    3 < 5    True
>=    Maior ou igual a    5 >= 5    True
<=    Menor ou igual a    3 <= 5    True
"""

a = True
b = False

print(a, b)

a and b

c = a and b
print(c)
c = a & b
print(c)

d = a or b
print(d)
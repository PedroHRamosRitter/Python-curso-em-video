from math import sqrt, hypot
co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto oposto: '))
h=hypot(co, ca)
# h= sqrt(co**2 + ca**2)
# h= (co**2+ ca**2) **(1/2) sem usar importação
print('A hipotenusa vai medir {:.2f}' .format(h))
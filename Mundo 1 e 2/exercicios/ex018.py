# import math
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja:'))
seno =sin(radians(angulo))
# seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}' .format(angulo, seno))
cosseno = cos(radians(angulo))
# cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o cosseno de {:.2f}' .format(angulo, cosseno))
tangente = tan(radians(angulo))
# tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a tangente de {:.2f}' .format(angulo, tangente))
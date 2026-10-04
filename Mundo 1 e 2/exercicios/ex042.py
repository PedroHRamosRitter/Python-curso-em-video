print('Analisador de Triângulos')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!', end=' ')
    # Quando eu coloco o end estou dizendo que que não vai ter enter no final da linha e quando coloco espaço no entre aspas vai ter um espaço
    if r1 == r2 == r3:
    # if r1 == r2 and r2 == r3:
    # Também pode se fazer assim sendo o jeito tradicional pois se r1 == r2 logicamente se r2 == r3 logo r3 == r1
        print('O triângulo é Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo é Isósceles')
    # else:
    #     print('O triângulo é Escaleno')
    elif r1 != r2 != r3 != r1:
     print('Escaleno')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulo')
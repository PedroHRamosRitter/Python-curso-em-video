c=float(input('Informe a temperatura em ºC:'))
f=((9*c)/5)+32
# f=celsius * (9/5) +32  tambem pode fazer assim
k=c+273.15

print('A temperatura de {}ºC corresponde a {}ºF e {}K!' .format(c, f, k))
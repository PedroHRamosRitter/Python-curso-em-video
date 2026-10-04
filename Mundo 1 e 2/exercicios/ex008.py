m= float(input('Digite um número em metros:'))
km= m/1000
hm= m/100
dam= m/10
dm= m*10
cm= m*100
mm= m*1000

print('A medida de {}m corresponde a \n {}km \n {}hm \n {}dam \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm ' .format(m, km, hm, dam, dm, cm, mm ))

# Quando fazer isto {:.0f} nas chaves tu exlcui a ''virgula'' no caso o ponto
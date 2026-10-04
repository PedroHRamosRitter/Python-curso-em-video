from datetime import date

ano = int(input('Qual o ano do seu nascimento? '))
anoatual = date.today().year
idade = date.today().year - ano
tempofalta = 18 - idade
tempopassou = idade - 18

if idade<18:
    print('Ainda você terá que se alistar no serviço militar, faltam {} anos para você se alistar.'.format(tempofalta))
    anoalistamento = anoatual + tempofalta
    print('Seu alistamento será em {}'.format(anoalistamento))
elif idade == 18:
    print('É hora de se alista no serviço militar.')
else:
    print('Já passou o tempo do alistamento militar, já passou {} anos do seu alistamento.'.format(tempopassou))
    anoalistamento = anoatual - tempopassou
    print('Seu alistamento foi em {}'.format(anoalistamento))


from lxml.doctestcompare import strip

frase = 'Curso em Vídeo Python'
print(frase)
print(frase[0:14])
# Numa string quando se conta começa certo mas no final é menos um ou seja é de 0 a 13
print(frase[:14])
print(frase[::2])
print(frase.count('O'))
print(frase.upper().count('O'))
print(frase.lower().count('o'))
print(frase.lower().find('vídeo'))
print(len(frase))
print(frase.replace('Python', 'Android',))  #Ele troca na frase onde tiver Python por Android
# para o replace alterar você tem que colocar frase = print(frase.replace('Python', 'Android',))
print('Curso' in frase)
print('curso' in frase)
# Diz se a palavra curso existe na frase
# No Python maiúsculo e minúsculo são diferentes
frase2 = frase.split()
print(' '.join(frase))
print('-'.join(frase2))

print(frase.find('Curso'))
# mostra a posição em que se encontra a palavra 'Curso', se mostrar -1 quer dizer que não existe

# strip() = Tira os espaços inuteis antes e depois da frase como por exemplo ' Curso em Vídeo em Python    ' tem um monte de espaços inutéis
# Ja o lstrip()   rstrip() tira os espaços inutéis no lado esquerdo ou direito se colocar L é de left e r de right
# No Python maiúsculo e minúsculo são diferentes


print("""Welcome! Are you completely new to programming?
about why and how to get started with Python. Fortunately
an experienced programmer in ny programming language
(whatever it may be) can pick up Python very quickly).
Its also easy for beginners to use and learn, so jum in!""")
# Aqui eu fiz o seguinte usei 3 aspas duplas pra não precisar fazer print linha por linha eu so fiz uma vez usando 3 aspas duplas
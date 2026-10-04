from hashlib import sha256

# SHA = Scure Hash Algorithm
texto = "Gafanhoto"
cod = texto.encode('utf-8')
hash = sha256(cod).hexdigest() # hexadecimal 0, 9, a, f


print(hash)
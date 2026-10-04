import urllib
import urllib.request
url = 'https://www.google.com'

try:
    site = urllib.request.urlopen(url, timeout = 5)
except urllib.error.URLError:
    print(f'\033[1;31mO site {url} não está acessível no momento.\033[m')
else:
    print(f'\033[1;32mConsegui acessar o site {url} com sucesso!\033[m')
    print(site.read()) # Código inteiro do google html
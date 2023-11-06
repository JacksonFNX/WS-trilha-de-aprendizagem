import requests
from bs4 import BeautifulSoup

#Esse código basicamente faz uma busca no google da cotação do dolar no momento e a imprime

# A variavel headers serve para mostrar ao navegador como eu quero visualiza-lo, pois para diferentes dispositivos a exibição pode ser diferente, nesse caso como estou utilizando o beautiful soup que interpreta e segue um caminho de tags específicas de HTMl, caso essa especificação não fosse feita, possivelmente haveriam caminhos diferentes para o mesmo lugar

link ="https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
    
request = requests.get(link, headers=headers)
print(request)
#print(request.text)
site = BeautifulSoup(request.text, "html.parser")

title = site.find("title")
print(title)

cotacaodolar = site.find("span", class_="SwHCTb")
print(cotacaodolar.get_text())
print(cotacaodolar["data-value"])


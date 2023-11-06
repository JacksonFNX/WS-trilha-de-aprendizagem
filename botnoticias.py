import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd

#Nesse código foi utilizado as duas bibliotecas utilizadas nos outros dois códigos. Esses frameworks são geralmente utilizados para manipulaçao e interpretação de dados de um site "estático", para uma navegação mais profunda e e interativa, normalmente se utiliza outros frameworks como o Selenium.
lista_noticias = []

response = requests.get("https://g1.globo.com/")

content = response.content

site = BeautifulSoup(content, 'html.parser')

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

print()
print("Notícias G1", date.today())
print()
for noticia in noticias:

        
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    print("Título: ")
    print(titulo.text)
    try:
        print(titulo['href'])
    except:
        print("link não encontrado")
    subtitulo = noticia.find('a', attrs={'class': 'bstn-relatedtext'})

    if subtitulo and titulo['href']:
        print("Subtitulo: ")
        print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        print("Nenhum subtitulo foi encontrado")
        lista_noticias.append([titulo.text, 'Nenhum subtitulo foi encontrado', 'Nenhum link foi encontrado'])
        
        
news = pd.DataFrame(lista_noticias, columns=['Título','Subtítulo', 'Link'])
data = date.today()
today = data.strftime('%d-%m-%Y')
nome = 'Noticias G1.xlsx'
news.to_excel(f'{today} - {nome}', index = False)
print(news)
import pandas as pd
#Este código tranforma tabelas HTML em tabelas xlsx, utiliziei duas tabelas diferentes de dois sites, porem pode-se adaptar para outros tipos de tabela também.

#o pandas funciona de forma parecida com o Beautifulsoup porem tem algumas funções mais específicas para transformação e visualizaçaõ de dados, ele é muito util principalmente quando utilizado em conjunto com outros frameworks como o selenium e o prorpio Beautifulsoup.

cotacaomateriais = "https://www.depositomarmeleiro.com.br/tabelas-preco/"

html = pd.read_html(cotacaomateriais)
cotacao = html[0]
print(cotacao)
dataframe = cotacao
dataframe.to_excel(r"D:\Users\vinga\Documents\Fabrica de Software\WSL\pandas\cotacao.xlsx")

reciclavel =  "https://www.reciclaecologica.com.br/blog/tabela-com-a-lista-de-materiais-que-podem-ser-reciclados"

html = pd.read_html(reciclavel, match="reciclável")
rec = html[0]
print(rec)
rec.to_excel(r"D:\Users\vinga\Documents\Fabrica de Software\WSL\pandas\rec.xlsx")










# coleta =  "https://www.joaopessoa.pb.gov.br/servico/calendario-de-coleta-domiciliar/"

# html = pd.read_html(coleta)
# col = html[0]
# print(rec)
# col.to_excel(r"D:\Users\vinga\Documents\Fabrica de Software\WSL\pandas\clc.xlsx")
# print("Arquivo salvo!")
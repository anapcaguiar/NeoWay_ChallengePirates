#Declarando URL
url = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"

#-----------------------------------------------------------------#
#---------Extraindo lista de estados do site dos correios---------#
#-----------------------------------------------------------------#

#Importando bibliotecas
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Extraindo o html
html = urlopen(url)
bsobj = BeautifulSoup(html, "html.parser")

#Localizar qualquer tag que tenha a propriedade class igual a f1col
teste = bsobj.find_all(class_="f1col")

#Tranformar em string
texto = str(teste)

#Verificar padrão
import re
padrao = re.compile('[A-Z]{2}')

#Extrair padrão 
resultado = re.findall(padrao, texto)

#Remover duplicatas
import numpy as np
estados = np.unique(resultado)

#Remover cabeçalho
indices = np.where(estados=='UF')
estados = np.delete(estados, indices)

#-----------------------------------------------------------------#
#---------Criar lista de consulta de estado e localidade ---------#
#-----------------------------------------------------------------#

ListaEstadosLocalidade = []
for estado in estados:
    post_fields = {"UF": estado, "Localidade" : " "}
    ListaEstadosLocalidade.append(post_fields)

#-----------------------------------------------------------------#
#--------- Consultar faixa de cep de todos os estados    ----------#
#---------  e concatenar dados em uma lista unica       ----------#
#-----------------------------------------------------------------#

#Bibliotecas
from importlib.abc import Finder
from urllib import request
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import pandas as pd

#Lê a primeira página tabela gerada por estado e adiciona a uma lista
FaixaCEP_TodosEstados = []
for post_fields in ListaEstadosLocalidade:
    fields = []
    request = Request(url, urlencode(post_fields).encode())
    result = urlopen(request).read()
    fields.append(result)
    FaixaCEP_TodosEstados.append(fields)

#Transformar em string
FaixaCEP_TodosEstados = str(FaixaCEP_TodosEstados)

#Leitura de caracter especial
result = bytes(FaixaCEP_TodosEstados, "iso-8859-1").decode("unicode_escape")

#Extrair lista com dados de todos os estados
dfs = pd.read_html(result)

# Aqui extraimos os estados
dfs_uf = [i for i in dfs if "UF" in i.columns.tolist()]
dfs_uf = pd.concat(dfs_uf).reset_index(drop=True)

# Aqui extraimos os municipios
dfs_mun = [i for i in dfs if "Localidade" in i.columns.tolist()]
dfs_mun = pd.concat(dfs_mun).reset_index(drop=True)

#-----------------------------------------------------------------#
#---------            Limpeza do dataframe               ---------#
#-----------------------------------------------------------------#

#Remover colunas desnecessárias
dfs_mun = dfs_mun.drop(columns=['Situação', 'Tipo de Faixa'])

#Adicionar identificador único
dfs_mun['ID'] = dfs_mun['Faixa de CEP'].str.split(" ", n=1, expand=True)[0]

#Remover valores duplicados
dfs_mun.drop_duplicates(subset ="ID", keep = False, inplace = True)

#-----------------------------------------------------------------#
#---------            Transformar em JSON                ---------#
#-----------------------------------------------------------------#

#Transformar em json
dfs_mun_json = dfs_mun.to_json()
print(dfs_mun_json)
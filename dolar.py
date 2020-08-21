import json
import requests

#################################################
#   Cotação Dólar e Euro                        #
#   Data do código: 21-ago-2020                 #
#   Autor: Giancarlo Rigotto                    #
#   Descrição: Script que será usado            #
#       futuramente em API. Coleta dados do     # 
#       portal do Banco Central do Brasil       #
#       para retornar valores atualizados       #
#       das moedas Euro e Dólar                 #
#################################################

#Link para API do BCB que retorna JSON com cotação atual de moedas
url = "https://www.bcb.gov.br/api/servico/sitebcb/indicadorCambio/"

#Tratamento do JSON
reponse = requests.get(url)
dados = json.loads(reponse.text)
lista = dados.get('conteudo')

#Separação em dicionários para Fechamento de Dólar e Euro:
dictDolar = lista[0]
dictEuro = lista[2]

######Elementos do Dicionário######
## moeda :
## valorCompra :
## valorVenda :
## dataIndicador:
## tipoCotacao :
## urlEdicaoItem :
## urlEdicaoLista :
###################################

#Prints para Simples Conferencia
print("Valor Dólar: R$ ",dictDolar["valorCompra"])
print("Valor Euro: R$ ",dictEuro["valorCompra"])
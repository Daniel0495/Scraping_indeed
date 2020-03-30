import pandas as pd

al = pd.read_json('data_indeed_Alemania.json')
ar = pd.read_json('data_indeed_Argentina.json')
ec = pd.read_json('data_indeed_Ecuador.json')
br = pd.read_json('data_indeed_Brasil.json')
ch = pd.read_json('data_indeed_Chile.json')
co = pd.read_json('data_indeed_Colombia.json')
cr = pd.read_json('data_indeed_Costa_Rica.json')
dn = pd.read_json('data_indeed_Dinamarca.json')
es = pd.read_json('data_indeed_España.json')
fn = pd.read_json('data_indeed_Finlandia.json')
id = pd.read_json('data_indeed_India.json')
mx = pd.read_json('data_indeed_México.json')
ng = pd.read_json('data_indeed_Noruega.json')
sc = pd.read_json('data_indeed_Suecia.json')
us = pd.read_json('data_indeed_USA.json')


al_lista =list(al['Alemania'])
ar_lista = list(ar['ARGENTINA'])
ec_lista = list(ec['Ecuador'])
br_lista = list(br['BRASIL'])
ch_lista = list(ch['Chile'])
co_lista = list(co['Colombia'])
cr_lista = list(cr['Costa Rica'])
dn_lista = list(dn['Dinamarca'])
es_lista = list(es['España'])
fn_lista = list(fn['Finlandia'])
id_lista = list(id['India'])
mx_lista = list(mx['México'])
ng_lista = list(ng['Noruega'])
sc_lista = list(sc['Suecia'])
us_lista = list(us['USA'])

lista_listas = [ar_lista,
al_lista,
ec_lista,
br_lista,
ch_lista,
co_lista,
cr_lista,
dn_lista,
es_lista,
fn_lista,
id_lista,
mx_lista,
ng_lista,
sc_lista,
us_lista]

lista_juntos = list()
for element in lista_listas:
    lista_juntos.extend(element)







juntos = pd.Series(lista_juntos)
juntos.to_json('Scraping_Indeed_full.json')

#print(lista_juntos)
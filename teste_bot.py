import pandas as pd
import streamlit as st
import requests
import time
import json

def cor(valor):
    valor_float = float(valor)
    if  valor_float > 2:
        return "Verde"
    else:
        return "Preto"


def crash (Quantidade):
    crash_dados = []
    url = 'https://blaze.com/api/crash_games/recent'
    crash_dados_requisição = requests.get(url)
    crash_dados_tudo = json.loads(crash_dados_requisição.content)
    for y in range(Quantidade):
        crash_dados.append(crash_dados_tudo[y]['crash_point'])
    return crash_dados

def String_para_float (valor):
    for caracter in valor :
        if caracter == 'R' or caracter == '$':
            valor = valor.replace(caracter,'')
    valor = float(valor)
    return valor

estrategia = ["Preto"]
qtd_estg = len(estrategia)

vela1 = crash(1)
vela2 = crash(1)

st.title('Bot para analize de Velas\n\n')

while True:

    vela1 = crash(1)
    vela2 = crash(1)
    crash_dados_cor = list(map(cor,crash(qtd_estg)))
    if crash_dados_cor == estrategia:
        st.write('Entrada Encontrada!\n')
        st.write('Ultima vela: '+str(vela1))
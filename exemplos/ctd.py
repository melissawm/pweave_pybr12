# coding: utf-8

#' # Exemplo: manipulação de NaNs e limpeza de dados

#' Neste exemplo, usaremos um arquivo com muitos dados ausentes (representados por NaNs) para explorar o conceito de *filtros*. Além disso, vamos fazer um gráfico simples para representar os dados. Para isso, vamos usar duas bibliotecas importantes: Pandas (que já mencionamos) e matplotlib.

import pandas as pd

#' Primeiramente, vamos ler o arquivo usando tabs como separadores.

dados = pd.read_csv('data_from_odv_data_carbon-sse_after_correction_spikes_v3_O2_corr.txt', sep = '\t', lineterminator='\n')
print(dados)

#' Agora, vamos tentar identificar de quantas estações temos dados disponíveis.

print(dados.Station.head)

#' Queremos identificar quantas estações temos; para isso, vamos identificar todas as linhas em que a coluna Station tem valores válidos. Podemos fazer isso de duas maneiras: primeiro, vamos identificar todas as linhas em que a coluna Station contém NaNs:

print(dados.Station.isnull().head)

#' Agora, vamos fazer o oposto: verificar quais linhas da coluna Station não tem NaNs:

print(dados.Station.notnull().head)

#' Podemos fazer um filtro: como o resultado da operação acima é uma coluna com valores Verdadeiro (True) ou Falso (False), podemos selecionar entre os dados apenas aquelas linhas para as quais a operação acima resultou em True. Isso é uma forma de slicing, mas como envolve uma operação lógica (algo que retorna verdadeiro ou falso) chamamos isso de **filtro**:

print(dados[dados.Station.notnull()])

#' Desta forma, o resultado acima nos retorna todas as linhas da planilha dados que contém informações sobre estações; de fato, cada linha acima corresponde a uma estação.

estacoes = dados[dados.Station.notnull()]

#' Podemos investigar os índices desta nova tabela estacoes (a coluna mais à esquerda mostrada acima, que não faz parte da tabela, mas é um índice criado pelo Pandas para acessar os elementos da tabela)

print(estacoes.index)

#' Observe que os índices da tabela estacoes ainda se referem aos índices das linhas correspondentes na tabela original! Isso ocorre pois extraímos a tabela estacoes da tabela dados.

#' Agora, vamos analisar o que acontece apenas na primeira estação; para isso, vamos selecionar da tabela original apenas as linhas que estão entre as informações da estação 1 e as informações da estação 2 (lembrando que os índices do Python iniciam-se no zero). Usando o método loc e salvamos estes dados na nova tabela estacao1:

estacao1 = dados.loc[estacoes.index[0]+1:estacoes.index[1]-1,:]

#' Queremos extrair dos dados desta estação a média das medições de oxigênio na água.

print(estacao1.columns)

print(estacao1['Oxygen [ml l]'].mean())

#' Agora, vamos fazer um gráfico das medições, marcando a média calculada acima no gráfico.

import matplotlib.pyplot as plt
list(estacao1.index.values)
plt.plot(list(estacao1.index.values),estacao1['Oxygen [ml l]'])

#' Finalmente, vamos plotar nosso gráfico incluindo uma linha horizontal denotando a média dos valores. Calculamos a média usando o método mean do Pandas.

plt.plot(estacao1['Oxygen [ml l]'])
plt.axhline(y=estacao1['Oxygen [ml l]'].mean(), linestyle = "dashed", color = "r")
plt.title("Oxygen [ml l] for Station 1")
plt.show()



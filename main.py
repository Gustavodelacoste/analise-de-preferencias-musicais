import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv("Musicas_dados/dados_musicais.csv")


#converte a coluna para datatime 
df["Carimbo de data/hora"] = pd.to_datetime(df["Carimbo de data/hora"], dayfirst=True)

#converte a coluna para mostrar apenas a data 
df["Data"]= df["Carimbo de data/hora"].dt.date 

#Remove colunas desnecessarias
df.drop(columns =["email","Carimbo de data/hora"], inplace=True )

#Missing data
# Verificar valores nulos
print(df.isnull().sum())

# Preencher valores nulos com a média ou mediana (por exemplo, para idades)
df['idade'].fillna(df['idade'].median(), inplace=True)

# Ou remover linhas com valores nulos em colunas específicas
df.dropna(subset=['regiao', 'genero'], inplace=True)


#Filtragem 
#por genero
df_feminino = df[df['genero'] == 'Feminino']

df_masculino= df[df['genero'] == 'Masculino']

df_outro = df[df['genero'] == 'Outro']

#regiao
 #qual o genero musical mais popular por regiao
print(df.groupby('regiao')['generos_consumidos'].value_counts())
    #idade media dos participantes por regiao
print(df.groupby('regiao')['idade'].mean())

#por idade 
df_maiores_20 = df[df['idade'] > 20]

df_menores_20 = df[df['idade'] < 20]

# Contar valores por categoria
print(df['genero'].value_counts())

#validação dos dados
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

#visualiza as primeiras linhas
print(df.head())

# Verificar informações gerais (colunas, tipos, valores nulos)
print(df.info())

# Estatísticas descritivas (para colunas numéricas)
print(df.describe())

#salva os dados processados 
df.to_csv('Musicas_dados/dados_processados.csv', index=False)
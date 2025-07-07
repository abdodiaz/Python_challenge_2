import pandas as ps
import numpy as np
# Challenge 1 : Création et exploration d’un DataFrame

data=[["Amine", 28, "Casablanca"],["Lina", 22, "Rabat"],["Youssef", 35, "Fès"],["Salma", 30, "Casablanca"],["Nora", np.nan, "Tanger"]]
df=ps.DataFrame(data , columns=["Nom","Age","Ville"])
print(df)
print("---------------------")
print(df.head(n=5))
print("---------------------")
print(df.info())
print("---------------------")
print(df.describe())
print("---------------------------------------------------------------")
#Challenge 2 : Sélection et filtrage de données

selected_column= df['Ville']
print(selected_column)
select_age=df[df['Age']>25]
print("---------------------")
print(select_age)
print("---------------------")
select_wv=df.loc[df['Ville']=='Casablanca'][['Nom','Ville']]
print(select_wv)
print("---------------------------------------------------------------")
age=df["Age"]
d_n =2025-age
df["Année de Naissance"]=d_n
print(df)
print("---------------------")
df['Nom']=df['Nom'].str.upper()
print(df)
print("---------------------")
df=df.rename(columns={'Ville': 'Localisation'})
print(df)
#Challenge 4 : Gestion des valeurs manquantes
print("------------------------")
null = df.isnull()
print(null)
print("------------------------")
df=df.fillna(df["Age"].mean())
print(df)
# Challenge 5 : Tri et suppression
print("---------------------------------------------------------------")
# decroissant = df.sort_values(by='Age', ascending=False)
# print(decroissant)
print("------------------------")
df=df.drop('Année de Naissance',axis=1)
print(df)
print("------------------------")
df=df.drop(index=0)
print(df)
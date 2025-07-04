import numpy as np
temperatures = np.array([20.5, 22.1, 23.8, 25.2, 24.7, 23.9, 22.5, 21.8])

#Challenge : Analyse de Températures
moyenne = np.mean(temperatures)
mediane = np.median(temperatures)
ecart_type = np.std(temperatures)

# Normalisation de Données
normalized_data = (temperatures - moyenne)/ecart_type
# print (normalized_data)

#Comparaison de Tableaux
c1= np.array([5,10,18,22,30])
c2= np.array([18,6,3,22,10])
c=np.where(c1 != c2 )
print(c)
print(c1[c])
print(c2[c])

#Challenge : Opérations Matricielles

m1=np.array([[5,10],
             [7,8]])
m2=np.array([[3,5],
             [9,4]])

mul=np.dot(m1,m2)
print("--------------------------------")
print(mul)
t=np.transpose(mul)

print("--------------------------------")
print(t)

print("--------------------------------")

i=np.linalg.inv(mul)
print(i)

#Challenge : Sélection Basée sur Conditions


Conditions = np.array([10,51,10,3,7,8,12])

seuil = 12

Con_seuil = np.where(Conditions > seuil)

print(Con_seuil)

nouveau_array= Conditions[Con_seuil]
print(nouveau_array)
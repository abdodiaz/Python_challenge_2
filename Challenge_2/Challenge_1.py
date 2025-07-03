#Gestion d’un compte bancaire en POO
class CompteBancaire :
    def __init__(self,_nom_proprietaire):
        self._nom_proprietaire=_nom_proprietaire
        self._solde=0.0
    def deposer(self,montant):
      self._solde=+montant
      return self._solde
    
    def retirer(self,montant):
        if montant>self._solde :
          print("solde < montant")
        else :
          result= self._solde-montant
          return result
    def afficher_solde(self):
       solde = self._solde   
       nom = self._nom_proprietaire  
       print(f"nom :{nom}, solde : {solde}")
       
          
    
CompteBancaire = CompteBancaire("ahmed")
print(CompteBancaire.deposer(float(4)))
print(CompteBancaire.retirer(float(1)))
print(CompteBancaire.afficher_solde())
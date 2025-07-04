#Système de gestion d’école 

class Personne :
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    def afficher_infos(self):
        print(f"nom : {self.nom} , prenom : {self.prenom} , age : {self.age}")

Personne =Personne("aaaa","bbb",12)

class Etudiant(Personne):
    def __init__(self, nom, prenom, age,matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule
        self.note = []
    def ajouter_note(self,note):
        self.note.append(note)
    def moyen(self):
        summ=0
        count=0
        for i in self.note:
            count+=1
            summ=summ+i
        result= summ/count
    def afficher_infos(self):
        super().afficher_infos()
        print("matricule est : ", self.matricule)
        print("moyenne est : " , self.result)

class Enseignant(Personne) :
    def __init__(self, nom, prenom, age,specialite,salaire):
        super().__init__(nom, prenom, age)
        self.specialite=specialite
        self.__salaire=salaire
    def afficher_infos() :
        super().afficher_infos()
        print("matricule est : ", self.specialite)
    def get_salaire(self):
        return self.__salaire
    def set_salaire(self,nsalaire):
        self.__salaire=nsalaire
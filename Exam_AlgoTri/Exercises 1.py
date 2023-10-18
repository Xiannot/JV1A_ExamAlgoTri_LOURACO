#Exercises 1:
#Consigne : 1/ Nous allons avoir besoin de permuter deux valeurs d’un tableau à partir de leurs indices.
#Écrire un programme permettant de permuter deux valeurs du tableau myTable.

#Variable et tableau :
myTable = [1,2,5,4,8]
stock = myTable[0]
#-------------------------
#opération de permutation
myTable[0] = myTable [4]
myTable[4] = stock
#-------------------------
#vérification du code
print (myTable)
#-------------------------
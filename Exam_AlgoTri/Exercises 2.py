#Exercises 2:
#consigne : 2/ Lors d’une seule itération, l'algorithme du tri à bulles parcourt le tableau, et compare les
#éléments consécutifs. Lorsque deux éléments consécutifs ne sont pas dans l'ordre, ils sont
#échangés. Par conséquent, à l’issue d’une itération (et donc, d’un parcours entier du
#tableau), le plus grand élément est systématiquement déplacé en fin de tableau ; comme s’il
#s’agissait d’une bulle qui remonte à la surface

#tableau
#--------------------------
myTable = [1,2,5,10,8]
ranger = []
#--------------------------
#Trie du tableau
#--------------------------
for i in range(5):
    val =min(myTable)
    stock =val
    position =myTable.index(val)
    myTable.pop(position)
    ranger.append(val)
#-------------------------
print(ranger)
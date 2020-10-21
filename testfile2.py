#Lire toutes les lignes d’un fichier à la fois en utilisant readlines()

# Ouvrir le fichier en lecture seule
file = open('level.txt', "r")
# utiliser readlines pour lire toutes les lignes du fichier
# La variable "lignes" est une liste contenant toutes les lignes du fichier
lines = file.readlines()
# fermez le fichier après avoir lu les lignes
file.close()

# Itérer sur les lignes
for line in lines:
    print(line.strip())

########################################################################
#Lire un fichier ligne par ligne en utilisant la boucle While

# Ouvrir le fichier en lecture seule
file = open('level.txt', "r")
# utilisez readline() pour lire la première ligne
line = file.readline()

while line:
    print(line)
    # utilisez readline() pour lire la ligne suivante
    line = file.readline()
file.close()

########################################################################
#Lire un fichier ligne par ligne en utilisant un itérateur

# Ouvrir le fichier en lecture seule
file = open('level.txt', "r")
for line in file:
    print(line)
file.close()

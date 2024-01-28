import os

chemin_complet = __file__
nom_fichier = os.path.basename(chemin_complet) #os.path.basename prend le chemin complet en argument et renvoie le nom du fichier

print(nom_fichier)

import re

# Input d'utilisateur, Majuscule et Enlever espaces.
inp = re.sub(r"\s+", "", str(input("Entrez la cordonée Excel:")).upper())
p = True #Eviter erreur

#Separer Colonne et ligne
lst = re.match(r'([A-Za-z]+)(\d+)', inp).groups()
if len(lst) == 2: 
    if lst[0].isdigit:
        lgn = lst[1]
        cln = lst[0]
    else:
        lgn = lst[0]
        cln = lst[1]
else:
    p= False
    print("Erreur")

# Fonction pour calculer le nombre de la colonne.
def colnum(cln):
    n = 0
    for c in cln:
        n = n * 26 + 1 + ord(c) - ord('A')
    return n

# Print les resultats.
if p == True:
    print("Colonne= " + str(colnum(cln)))
    print("Ligne= " + lgn)

# Eviter que la console se ferme directement.
input("Appuyez Enter pour fermer cette fenetre.")

# Input d'utilisateur.
inp = input("Entrez la colonne et la ligne sérapés par un espace:")

# Separer Ligne.
ligne = [int(i) for i in inp.split() if i.isdigit()]

# Separer Colonne 
cln = [str(s) for s in inp.split() if s.isdigit() == False]
T = len(cln)
if T == 1:cln = cln[0] # Transformer la liste en variable.

# Fonction pour calculer le nombre de la colonne.
def colnum(cln):
    n = 0
    for c in cln:
        n = n * 26 + 1 + ord(c) - ord('A')
    return n

# Print les resultats.
print("Colonne= " + str(colnum(cln)))
print("Ligne= " + str(ligne[0]))

# Eviter que la console se ferme directement.
input("Appuyez Enter pour fermer cette fenetre.")
# Input de l'utilisateur.
n = int(input("Entrez un entier:"))
L = 0
if n > 0:print("Suite de Syracuse pour n={0}".format(n))

# Loop qui s'arrete quand n = 1.
while n != 1: 
    L = L+1
    if n == 0:  # Pour invalider 0.
        print("Ce nombre est invalide.")
        break
    elif n%2 == 0: # Si le nombre est pair donc on le divise par 2.
        print(n)
        n = n//2
    else: # Si le Nombre est impair on le multiplie par 3 et on ajout 1.
        print(n)
        n = 3*n + 1

# Print le nombre d'opérations + le "1".
if n == 1: 
    print(1)
    print("Suite terminée en {0} itérations".format(L))

# Eviter que le programme se ferme directement.
input("Appuyez Enter pour sortir de cette fenetre.")

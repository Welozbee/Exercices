n = int(input("Entrez un entier:"))
if n > 0:print("Suite de Syracuse pour n={0}".format(n))
L = 0 
while n != 1: 
    L = L+1
    if n == 0: 
        print("Ce nombre est invalide.")
        break
    elif n%2 == 0: 
        print(n)
        n = n//2
    else: 
        print(n)
        n = 3*n + 1           
if n == 1: 
    print(1)
    print("Suite terminée en {0} itérations".format(L))

input("Appuyez enter pour sortir de cette fenetre.")
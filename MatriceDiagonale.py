#   NOUBISSIE KAMGA WILFRIED
#   20U2671

#coding:utf-8

M = [[0,0,0],[0,0,0],[0,0,0]] 
valeursPropre = []

print("DIAGONALISATION DE MATRICES D'ORDRE 3".center(70,"-"))
print("\n\tVeuillez entrer votre matrice.(Les elements de la matrice seront enregistres ligne par ligne)\n\n")

for i in range(3):
    for j in range(3):
        M[i][j] = int(input("Element [{}][{}] : ".format(i,j)))

print("\nSoit A la matrice definie par : \n")

for i in range(3):
    for j in range(3):
        print(M[i][j],end="\t")
    print("\n")

#---------------Recherche des valeurs propres-------------#

k = -1000

while k<=1000:
    if ((M[0][0]-k)*(M[1][1]-k)*(M[2][2]-k) - (M[2][1]*M[1][2])*(M[0][0]-k) - (M[0][1]*M[1][0]*(M[2][2]-k)) + (M[0][1]*M[2][0]*M[1][2]) + (M[0][2]*M[1][0]*M[2][1]) - (M[2][0]*M[0][2])*(M[1][1]-k)) == 0:
        valeursPropre.append(k)
    k += 1

print("Les valeurs propres (reelles) associees a la matrice A sont : ",end=" ")
for valeur in valeursPropre:
    print(valeur,end="  ")
print("\n")

print("Donc Spec(A) = {",end=" ")
for valeur in valeursPropre:
    print(valeur,end=";  ")
print("}\n")

#---------------Verification des conditions de diagonalisation-------------#

if len(valeursPropre) < 3:
    print("La matrice A possedant moins de 3 valeurs propres(distinctes), elle n'est donc pas diagonalisable\n")

else:
    D = [[0,0,0],[0,0,0],[0,0,0]]
    P = [[0,0,0],[0,0,0],[0,0,0]]

    D[0][0] = valeursPropre[0]
    D[1][1] = valeursPropre[1]
    D[2][2] = valeursPropre[2]
    print("La matrice A est diagonalisable, avec comme matrice diagonale la matrice D definie par:\n")
    for i in range(3):
        for j in range(3):
            print(D[i][j],end="\t")
        print("\n")

#---------------Recherche de la matrice de passage-------------#
    try:
        E0 = [0,0,1]
        E1 = [0,0,1]
        E2 = [0,0,1]

        E0[0] = (((M[0][0]-valeursPropre[0])*(M[1][1]-valeursPropre[0])*M[0][2] - M[0][1]*M[1][0]*M[0][2]) + M[0][1]*M[0][2]*M[1][0] - (M[1][2]*(M[0][0]-valeursPropre[0])*M[0][1])) / (((M[0][0]-valeursPropre[0])*M[0][1]*M[1][0]) - ((M[0][0]-valeursPropre[0])*(M[0][0]-valeursPropre[0])*(M[1][1]-valeursPropre[0])))
        E0[1] = ((M[1][2]*(M[0][0]-valeursPropre[0])) - M[0][2]*M[1][0]) / (M[0][1]*M[1][0] - ((M[0][0]-valeursPropre[0])*(M[1][1]-valeursPropre[0])))

        E1[0] = (((M[0][0]-valeursPropre[1])*(M[1][1]-valeursPropre[1])*M[0][2] - M[0][1]*M[1][0]*M[0][2]) + M[0][1]*M[0][2]*M[1][0] - (M[1][2]*(M[0][0]-valeursPropre[1])*M[0][1])) / (((M[0][0]-valeursPropre[1])*M[0][1]*M[1][0]) - ((M[0][0]-valeursPropre[1])*(M[0][0]-valeursPropre[1])*(M[1][1]-valeursPropre[1])))
        E1[1] = ((M[1][2]*(M[0][0]-valeursPropre[1])) - M[0][2]*M[1][0]) / (M[0][1]*M[1][0] - ((M[0][0]-valeursPropre[1])*(M[1][1]-valeursPropre[1])))

        E2[0] = (((M[0][0]-valeursPropre[2])*(M[1][1]-valeursPropre[2])*M[0][2] - M[0][1]*M[1][0]*M[0][2]) + M[0][1]*M[0][2]*M[1][0] - (M[1][2]*(M[0][0]-valeursPropre[2])*M[0][1])) / (((M[0][0]-valeursPropre[2])*M[0][1]*M[1][0]) - ((M[0][0]-valeursPropre[2])*(M[0][0]-valeursPropre[2])*(M[1][1]-valeursPropre[2])))
        E2[1] = ((M[1][2]*(M[0][0]-valeursPropre[2])) - M[0][2]*M[1][0]) / (M[0][1]*M[1][0] - ((M[0][0]-valeursPropre[2])*(M[1][1]-valeursPropre[2])))


        P[0][0] = E0[0]
        P[1][0] = E0[1]
        P[2][0] = E0[2]

        P[0][1] = E1[0]
        P[1][1] = E1[1]
        P[2][1] = E1[2]

        P[0][2] = E2[0]
        P[1][2] = E2[1]
        P[2][2] = E2[2]

        print("Et avec comme matrice de passage la matrice P, definie par : \n")

        for i in range(3):
            for j in range(3):
                print(P[i][j],end="\t")
            print("\n")
    
    except ZeroDivisionError:
        pass
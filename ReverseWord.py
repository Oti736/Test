#Exercitiul de reverse la un sir
sir1 = input("Introduceti sirul: ")
#separam sirul in cuvinte
cuv = sir1.split()
#creeam un vector gol pentru fiecare cuvant 
rev_sir1 = []
for i in cuv: 
    rev_sir1.append(i[::-1])

sir2 = " ".join(rev_sir1)

print("Sirul inversat este: ", sir2) 

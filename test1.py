
name = []
cont = 0
while cont != 3:
    nom =(input("Ingrese un nombre :"))
    name.append(nom)
    cont +=1
nl = ""
for n in name:
    if len(name) > len(nl):
        nl = n   
print(f"el nombre mas largo es {nl}")

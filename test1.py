
name = []
cont = 0
while cont != 3:
    nom =(input("Ingrese un nombre :"))
    name.append(nom)
    cont +=1
nl = ""
print("Imprimiendo mi primera colaboración")
for n in name:
    if len(name) > len(nl):
        nl = n + "s"  
print(f"el nombre mas largo es {nl}")

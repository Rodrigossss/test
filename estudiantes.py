import csv 
with open('estudiantes_archivo.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
#    escritor_csv.writerow(['Nombre', 'p1',"p2","p3","a1","a2","a3","a4","a5"])
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows([["AGUIRRE HENRIQUEZ JAVIERA ANDREA","50","37","70","1","0","0","1","1"],
                            ["ALBORNOZ SEPULVEDA JOSE IGNACIO","56","35","48","0","1","1","1","1"],
                            ["ALVIAL ZAMORANO MARCO ISAIAS","20","35","70","1","1","0","0","1"],
                            ["ARANCIBIA VERA VALESKA DESIREE","45","10","55","0","1","1","0","0"],
                            ["AREVALO GUERRA CRISTOBAL VICTOR","55","67","41","1","0","0","1","1"],
                            ["DIAZ GODOY CONSTANZA","33","34","56","0","1","0","1","1"],
                            ["FAGUAS ESTAY ALEJANDRA FRANCISCA","56","70","66","0","1","1","0","0"],
                            ["FUENTES ROJAS DAVID","12","45","68","0","0","1","1","1"],
                            ["GARCIA NAVARRETE SEBASTIAN ANDRES","49","55","70","0","0","0","1","1"]
                            ])
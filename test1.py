
import csv
notas=[]
def calcular_np(notas):
    for nota in notas:
        np = (nota*0.30)+(nota*0.35)+(nota*0.35)
        return print(np)

def ri(asistencia):
    for dia in asistencia:
        promedio=(dia+dia+dia+dia+dia+dia+dia)/7
        if promedio>=0.65:
            return print("aprobó")
        else:
            return print("reprobó")
#        
#def np_ri_actualizado (np, ri):
#    with open ('ista.csv', 'w', newline='') as ista_csv:
#        escritor_csv=csv.writer(ista_csv)
#        escritor_csv.writerow([nombre, nota, asistencia])
#
                
with open ('estudiantes_archivo.csv', 'r', newline='') as estudiantes_archivo_csv:
    reader= csv.reader(estudiantes_archivo_csv)
    for fila in reader:
        for columna in fila[1]:
            notas.append(columna)

print(notas)
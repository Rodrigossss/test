
import csv
p1=[]
p2=[]
p3=[]
asistencia=[]
nombre=[]
estudiante=[]
notas=[]
np=[]

     
#def calcular_np(notas):
#    for nota in p1:
#        nota= float(nota)
#        n1 = (nota*0.30)
#    for nota in p2:
#        nota= float(nota)
#        n2 = (nota*0.35)
#    for nota in p3:
#        nota= float(nota)
#        n3 = (nota*0.35)
#    np=(n1+n2+n3)
#    return print(np)
        

def ri(asistencia):
        for dia in (asistencia):
            dia=int(dia)
            promedio=(dia+dia+dia+dia+dia)/5
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
        estudiante.append(fila)
       # nombre.append(fila[0])
       # p1.append(fila[1])
       # p2.append(fila[2])
       # p3.append(fila[3])
        #p4=p1+p2+p3
        #calcular_np(p1, p2, p3)
        #asistencia.append(fila[4])
        #asistencia.append(fila[5])
        #asistencia.append(fila[6])
        #asistencia.append(fila[7])
        #asistencia.append(fila[8])
        #ri(asistencia)


#print(p1, p2, p3)
#print(asistencia)
#print(nombre)
#print(estudiante[0])
#for lista in estudiante:
#    notas=lista[1:4]
#    print(notas)
for lista in estudiante:
    notas=lista[1:4]
    #print(notas)
for nota in notas:
     nota=int((nota))
     nota1= nota[0]*0.30
     nota2= nota[1]*0.35
     nota3= nota[2]*0.35
     #np.append(nota1+nota2+nota3)
print(nota[0]*0.30)
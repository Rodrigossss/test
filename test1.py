def calcular_np(p1, p2, p3):
    np = p1*0.30+p2*0.35+p3*0.35
    return print(np)

def ri(asistencia):
    for dia in asistencia:
        promedio=(dia+dia+dia+dia+dia+dia+dia)/7
        if promedio>=0.65:
            return print("aprobó")
        else:
            return print("reprobó")
        
def np_ri_actualizado (np, ri):
    with open ('ista.csv', 'w', newline='') as ista_csv:
        escritor_csv=csv.writer(ista_csv)
        escritor_csv.writerow([nombre, nota, asistencia])

                

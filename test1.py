asistencia=[1,1,1,1,1,1,1]

def ri(asistencia):
    for dia in asistencia:
        promedio=(dia+dia+dia+dia+dia+dia+dia)/7
        if promedio>=0.65:
            return print("aprobó")
        else:
            return print("reprobó")
        
ri(asistencia)

                

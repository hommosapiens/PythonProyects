p1 = float(input("Nota primer parcial: "))
p2 = float(input("Nota segundo parcial: "))
p3 = float(input("Nota tercero parcial: "))

porcentajeParciales = ((p1+p2+p3)/3)*0.55

examenFinal = float(input("Nota del examen final: "))
porcentajeExamFinal = examenFinal*0.30

trabajoFinal = float(input("Nota del examen final: "))
porcentajeTrabajoFinal = trabajoFinal*0.15

print("Tu nota final es %.2f" % (porcentajeParciales+porcentajeExamFinal+porcentajeTrabajoFinal))

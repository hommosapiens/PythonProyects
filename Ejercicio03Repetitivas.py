n = int(input("Introduzca un numero: "))
t = 0
c = 0
while n != 0:
    t += n
    c += 1
    
    n = int(input("Introduzca un numero: "))
    
    if n == 0:
        print("Suma total de los numeros: %f\nMedia total de los numeros = %f " %(t,(t/c)))
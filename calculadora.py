def sumar(numero1, numero2):
    resultado_suma = numero1 + numero2
    print(resultado_suma)
    return resultado_suma


def restar(numero1, numero2):
    resultado_resta = (numero1 - numero2)
    print(resultado_resta)
    return resultado_resta

def producto(numero1, numero2):
    resultado_producto = (numero1 * numero2)
    print(resultado_producto)
    return resultado_producto

def division(numerador, denominador):
    resultado_cociente = (numerador / denominador)
    print(resultado_cociente)
    return resultado_cociente

print("Sumas")
sumar(1,4)
sumar(55, 49)
sumar(10, 25)

print("Restas")
restar(4,3)
restar(120,65)
restar(31,17)

print("Productos")
producto(4,3)
producto(7,8)
producto(10,3)

print("Divisiones")
division(16,8)
division(32,4)
division(84,6)
eleccion=input("Para iniciar ingrese 'i', para finalizar ingrese 'f': ")
compra=[]
total=0
valor=False
if eleccion == "i":
    valor=True
else:
    valor=False

while valor == True:
    producto, cantidad, precio=input("Ingrese el nombre del producto, la cantidad en kg y el precio ")
    total=total + float(cantidad)*float(precio)
    compra.append([producto, cantidad, precio])
    eleccion=input("Para agregar otro producto ingrese 'i', para finalizar ingrese cualquier otro caracter ")
    if eleccion == "i":
        valor=True
    else:
        valor=False

print("El total de la compra es ",total)
print(compra)
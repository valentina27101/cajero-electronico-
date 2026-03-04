Saldo = 1000 #Saldo inicial

print("Cajero electrónico")
print("Seleccione su operación:")
print("1.Consultar saldo")
print("2.Pagos")
print("3.Retiro")
print("4.Deposito")
print("5.Salir")
    
Opcion = int(input("Escoja una opción \n"))

if Opcion == 1:
    print ("su saldo actual es: ", Saldo)

elif Opcion == 2: 
    pago = float(input("ingrese el valor a pagar: "))
    if pago <= Saldo:
        Saldo -= pago 
        print("pago realizado con exito.")
        print("su nuevo saldo es: ", Saldo)

    else:
        print("saldo insuficiente.")
    
elif Opcion == 3:
    retiro = float(input("Ingrese el valor a retirar: "))
    if retiro <= Saldo:
        Saldo -= retiro
        print("Retiro exitoso.")
        print("Su nuevo saldo es:", Saldo)
    else:
        print("Saldo insuficiente.")

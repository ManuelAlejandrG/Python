def calculadora():
    funcion=int(input("Ingrese la opcion que desea ejecutar: \n"
                     "1) si desea sumar dos numeros \n"
                     "2) si desea multiplicar dos numeros \n"))
    while funcion not in [1,2,3,4]:
        print("Ha seleccionado un numero incorrecto, seleccione de nuevo")
        funcion=int(input("Ingrese la opcion que desea ejecutar: \n"
                     "1) si desea sumar dos numeros \n"
                     "2) si desea multiplicar dos numeros \n"))
                    
    if funcion==1:
        numero1=float(input("Seleccione el primer numero: "))
        numero2=float(input("Seleccione el segundo numero: "))
        suma(numero1,numero2)
    
    if funcion==2:
        numero1=float(input("Seleccione el primer numero: "))
        numero2=float(input("Seleccione el segundo numero: "))
        multiplica(numero1,numero2)
        

        
def suma(a,b):
    print("El resultado es: " + str(a+b))
    agregar=int(input("Desea realizar otra operacion:\n "
                     "1) Si \n "
                     "2) No "))
    while agregar not in [1,2]:
        print("Ha seleccionado un numero incorrecto, seleccione de nuevo")
        agregar=int(input("Desea realizar otra operacion:\n "
                     "1) Si \n "
                     "2) No "))
    if agregar==1:
        calculadora()
    else:
        print("Gracias por usar nuestra calculadora")
def multiplica(a,b):
    print("El resultado es: "+  str(a*b))
    agregar=int(input("Desea realizar otra operacion: \n"
                     "1) Si \n "
                     "2) No "))
    while agregar not in [1,2]:
        print("Ha seleccionado un numero incorrecto, seleccione de nuevo")
        agregar=int(input("Desea realizar otra operacion:\n "
                     "1) Si \n "
                     "2) No "))
    if agregar==1:
        calculadora()
    else:
        print("Gracias por usar nuestra calculadora")
    
                          
                        
                          
                          
calculadora()

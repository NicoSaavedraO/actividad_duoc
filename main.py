import os
os.system("cls")
# ETAPAS:
# Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.

#edad = int
#try:
#    edad = int(input("Ingrese su edad:\n"))
#    if edad >= 18:
#        print("Usted es mayor de edad.")
#    else:
#        print("Usted es menor de edad.")
#except:
#    print("Edad ingresada inválida.")

# Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
# User1: pedro   	Contraseña1: 1234
# User2: angel		Contraseña2: a4s1

#try:
#    user1 = "pedro"
#    contrasena1 = "1234"
#    user2 = "angel"
#    contrasena2 = "a4s1"
#    user = input("Ingrese usuario:\n")
#    contra = input("Ingrese la contraseña:\n")
#    if user == user1 and contra == contrasena1 or user == user2 and contra == contrasena2:
#        print(f"Bienvenido {user}.")
#    else:
#        print(f"Credenciales incorrectas.")
#except:
#    print("No se pudo realizar la acción.")

#Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), 
# finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.

#cantidad = 3
#acum_nota = 0
#for x in range(cantidad):
#    nota = float(input(f"Ingrese nota {x+1}:\n"))
#    acum_nota = acum_nota + nota
#promedio = acum_nota / cantidad
#if promedio >= 4:
#    print(f"Felicidades aprobaste con un {promedio}.")
#else:
#    print(f"Lo lamento reprobaste con un {promedio}.")
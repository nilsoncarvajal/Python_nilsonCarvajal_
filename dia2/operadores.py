#hola usuario 

#1.Codigo Fibonacci

print("Hola, usuario vienvenido a mi programa =>")
print("---------------------------------------")
print("El código de Fibonacci se trata de una serie infinita de números naturales que empieza con un 0 y un 1 y continúa añadiendo números que son la suma de los dos anteriores ejemplo 0,1,1,2,3,5,8 etc...")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("")
input("ingresa tu número: ")

#con el bucle while podremos hacer que se repita el proceso si el usuario lo desea
continuar="C"
while continuar.lower()=="C":

numero=int(input("Ingresa un número,el cual sera representado hasta que el termino de la secuencia se termine: "))

A=0
B=1

print("")
#ciclo para los números
while A<89: #seran 11 números
    print(A)
    break

resultado=A+B

A=B
B=resultado

continuar=input("Deseas continuar con el programa?(si/no)")

if continuar.lower()=="n":

    print("")
    print("El programa ah finalizado")

#Desarrollado por Nilson Carvajal 


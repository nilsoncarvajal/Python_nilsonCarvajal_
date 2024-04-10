#-----------------------------------
#------Día 1 cheat sheet python-----
#-----------------------------------

#Imprimir Hola Mundo
print("Hola Mundo")


#Datos primitivos

#Número
numerito = 1 #nombreVariable = valor
print(numerito) #imprimir(variable)
print(type(numerito)) #imprimir(tipo(variable))

#Decimal
numeritoDecimal = 1.1
print(numeritoDecimal)
print(type(numeritoDecimal))

#Booleano
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito))

#Cadena de texto
texto = "Tibú"
print(texto)
print(type(texto))

#Ingresa por teclado la información (input)
nombre = input("Por favor, ingrese su nombre: ")


#Conversión de tipos de variables
edad = "22"
print(edad)
print(type(edad))

int_edad = int(edad)
print(int_edad + 2) 
print(type(int_edad))

#int a bool
num=11
print(num)
print(type(num))

boleano= bool(num)
print(boleano)
print(type(boleano))


#Bucles For y While

#While
i = 0
while i < 10 :
  print(i**2)  
  i = i + 1
  print ("fin del programa")

#For
for i in range(10) :
  print(i**2)

#Funciones de cuatro tipos

#funcion con un parárametro
def saludos(name) : 
  print("hola bro " + name + ",eres bello")

saludos("Nilson")

#funcion sin parametros o retornos de valores

def saluda() :
  print("hello")#llamamos la funcion y se mostrara en la consola
saluda()

  #funcion con múltiples parámetros con una sentencia de retorno
def resta(a , b) :
    resta= a - b
    return resta

rresta = resta(10 , 8)

print("El resultado de la resta es: ",rresta ), 


#funcion sin parametros pero con retorno

def resta() :
  return "4"
print("El resultado es",resta(),)  







#Desarollado por Nilson Carvajal T.I 1093907710
#Taller
#Algoritmo que nos permita cambiar dinero

def vueltos_persona(cantidad_monedas):

    vueltos = [] #Con cambio podemos guardar la cantidades de nuestras monedas

    cantidad_monedas_10 = cantidad_monedas // 10 #Vamos a calcular la cantidad de monedas de 10
    vueltos.append(10) #con .append podemos guardar nuestros datos en la variable creamos que es = a []
    cantidad_monedas -=  cantidad_monedas_10 * 10 

    cantidad_monedas_5 = cantidad_monedas // 5
    vueltos.append(5)
    cantidad_monedas -= cantidad_monedas_5 * 5

    cantidad_monedas_1 = cantidad_monedas // 1
    vueltos.append(1)
    cantidad_monedas -=  cantidad_monedas_1 * 1

    return vueltos

cantidad_monedas=int(input("Coloca tu número: "))
vueltos =vueltos_persona(cantidad_monedas)
print(f"PARA {cantidad_monedas}, el cambio es: {vueltos[0]} son monedas de 10, {vueltos[1]} son monedas de 5, {vueltos[2]} son monedas de 1 ")


    


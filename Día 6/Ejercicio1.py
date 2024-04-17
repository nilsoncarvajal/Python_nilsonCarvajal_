lista=[]

print("")
print("")
valor=int(input(""))

assert 0 < valor < 300,""

for i in range (0,valor):

    lista.append(input(""))
    lista = [int(x) for x in lista]

    duplex =list(set(lista))
    duplex.sort(key=int)
print(duplex) 

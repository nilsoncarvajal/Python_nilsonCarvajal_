l = []

print("")
print("")
valor = int(input(""))

assert 0 < valor < 300, ""

for i in range(0, valor):
    l.append(input(""))

# Convert input strings to integers for sorting
l = [int(x) for x in l]

duplex = list(set(l))
duplex.sort(key=int)  # Sorting the list in ascending order
print(duplex)

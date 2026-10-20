suma = 10000; i = 0 
while suma > 0:
    suma -= int(input("valoare vanzare ziua " + str(i+1) + " "))
    i += 1

print("vanzarea totala este de ", 10000 - suma)
print("suma este depasita cu ", - suma)
print("numarul de zile este ", i)

nr = 0; vTotal = 0; ceva = 0
for i in range(10):
    c, v = map(int, input("pret unitar si cantitate ").split())
    vanzariProdus = c*v
    print()
    if vanzariProdus > ceva:
        nr += 1
    vTotal += vanzariProdus



    
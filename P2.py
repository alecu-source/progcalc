nrZile = int(input("cate zile vrem? "))
nrPeste1000 = 0; suma = 0
for i in range(nrZile):
    x = float(input("incasare ziua " + str(i+1) + " "))
    suma += x
    if x > 1000:
        nrPeste1000 += 1

print("Suma incasarilor", suma)
print("Media zilelor", suma/nrZile)
print("Numarul de incasari peste 1000", nrPeste1000)    
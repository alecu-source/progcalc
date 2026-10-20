def salariu(ore):
    return min(ore, 40) * 15 + max(ore - 40, 0) * 22.5

def impozit(sal):
    s1 = min(400, sal)
    sal = sal - 400
    s2 = min(200, max(sal, 0))
    sal = sal - 200
    s3 = max(sal, 0)
    return s1 * 0.1 + s2 * 0.18 + s3 * 0.25

ore = int(input(" ore =  ? "))

salariuBrut = salariu(ore)
print("salariu brut = ", salariuBrut)
impozitLaSalariu = impozit(salariuBrut)
salariuNet = salariuBrut - impozitLaSalariu
print("impozit = ", impozitLaSalariu)
print("salariu net  = ", salariuNet)


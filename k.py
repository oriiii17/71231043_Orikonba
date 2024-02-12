Erika = 200000000
Deposito = 400000000
bunga = 0.1 
n = 1
t = 0

while Erika < Deposito :
    Erika = Erika * (1 + bunga/n)
    t += 1

print ("Waktu yang dibutuhkan :", t, "tahun")
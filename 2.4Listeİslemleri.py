liste=[12, 4, 9, 25, 30, 7, 18]
toplam=0
for i in liste:
    toplam +=i
ortalama=toplam/len(liste)
print("listenin ortalaması: ",ortalama)
buyukler=[]
for j in liste:
    if j>=ortalama:
        buyukler.append(j)
print("ortalamadan büyük olanlar.",buyukler)
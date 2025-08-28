Liste=[]
kosull= True
toplam=0
while kosull==True:
    girdi=int(input("Sayi Giriiz:"))
    Liste.append(girdi)
    if girdi==0 :
        kosull==False
        for i in Liste:
            toplam+=i
        print("Toplam:",toplam)
        print("Ortalama:",int(toplam/(len(Liste)-1)))
        print("Dögüden Çıkılıyor...")
        break
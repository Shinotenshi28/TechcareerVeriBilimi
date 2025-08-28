parola= input("Parolanizi Giriniz:")
sayiKontrol=0
buyukKontrol=0

for i in parola:
    if i.isupper():
        buyukKontrol=1

for j in parola:
    if j.isdigit():
        sayiKontrol=1
if len(parola)>=8:
    if buyukKontrol==1:
        if sayiKontrol==1:
            print("parolanız Olusruldu")
        else :
            print("Parolanızda en az 1 adet Rakam olmalı")
            
    else:
        print("parolanızda en az 1 adet büyük harf bulunmalı")
        
else :
    print("Parola en az 8 karakterden oluşmalıdır")
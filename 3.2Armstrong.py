girdi=int(input("Sayı giriniz:"))
if girdi<0:
    girdi*=(-1)
i=0
toplam=0
while i< len(str(girdi)):
    sayım=int((str(girdi))[i])
    toplam =(toplam + (sayım * sayım))
    i+=1
if toplam==girdi:
    print("girdiğiniz",girdi,"bir armstrong sayıdır")
else :
    print("girdiğiniz",girdi,"bir armstrong sayı değildir")
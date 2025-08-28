girdi=input("Kelimenizi giriniz")
tersi=girdi[::-1]
if girdi==tersi:
    print("Kelimeniz polindrom bir kelimedir.")
else:
    print("Girdiğiniz kelime polindrom değildir.")
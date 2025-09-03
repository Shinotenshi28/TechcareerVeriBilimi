import random
sayılar=list(range(1,101))

rastgeleler=list(random.sample(sayılar,10))
ort=0
i=0
toplam =0
while i < 10:
    toplam+=rastgeleler[i]
    i+=1
print(toplam/10)

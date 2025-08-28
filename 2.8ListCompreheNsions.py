i=0
Liste=[]
Kareler=[]
while i<=100:
    Liste.append(i) 
    i+=1
for j in Liste:
    if j%3==0 or j%5==0:
        Kareler.append(j*j)
print(Kareler)
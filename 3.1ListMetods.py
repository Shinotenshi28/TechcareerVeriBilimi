notlar = [85, 92, 76, 92, 100, 76, 85, 92]
i=0
while i < len(notlar):
    j = i + 1
    while j < len(notlar):
        if notlar[j] == notlar[i]:
            notlar.pop(j)   
        else:
            j += 1
    i += 1

print(notlar)
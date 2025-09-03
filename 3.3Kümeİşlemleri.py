A = {"Python", "R", "SQL", "Java"}
B = {"C++", "Python", "JavaScript", "SQL"}
C = set()  # Ortak 

A_list = list(A)
B_list = list(B)

i = 0
while i < len(A_list):
    elemanA = A_list[i]
    j = 0
    while j < len(B_list):
        elemanB = B_list[j]
        if elemanA == elemanB:
            C.add(elemanA)  
        j += 1
    i += 1
birlleşim= A|B
print(C) 
print("birleşim=",birlleşim)
l = [1,2,3,4,5,]
i = 4
while i >=0:
    print(l[i],end=" ")
    i -= 1
print()
for j in range(5):
    print(l[4-j],end=" ")
print()
print(l[::-1])
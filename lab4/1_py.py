mul = 1
count = 0
for i in range(100):
    if int(i) % 2 != 0:
        print(i,end=" ")
        count += 1
        if i < 50:
           mul *= i
        if count % 10 == 0:
            print()
print(mul)
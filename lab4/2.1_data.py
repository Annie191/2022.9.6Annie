import math
accuracy = 0.001
number = 1
while abs(math.pow(number,2) - 2) > accuracy:
    number += accuracy
print(number) 
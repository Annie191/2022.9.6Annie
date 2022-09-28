import random 
import math 
S = 2 * 2
N = 1000000
C = 0 
for i in range(N): 
    x = random.uniform(-1.0,1.0) 
    y = random.uniform(-1.0,1.0) 
    if math.pow(((math.pow(x,2) + math.pow(y,2))),1/2) <= 1: 
        C += 1 
I = C / N * S
print("%.10f" %I)
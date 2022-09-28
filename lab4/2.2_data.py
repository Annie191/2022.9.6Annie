def Square_root_2():
    i = 0
    c = 2
    max = c
    min = 0
    g = (max + min) / 2
    while(abs(g * g - c) > 0.00000001):
        if (g * g < c):
            min = g
        else:
            max = g
        g = (max + min) / 2
    print(g)
Square_root_2()
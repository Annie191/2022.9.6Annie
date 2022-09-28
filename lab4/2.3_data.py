def square_root_2():
    k = 2 
    x = 2.0 #当前迭代的x
    y = 0.0;  #上一次的迭代结果
    #两次迭代的差值非常小时，便接近结果了
    while (abs(x - y) > 0.00001):
        #保存上一次迭代的结果
        y = x
        #求解新的x
        x = (x * x + k) / (2 * x)
    print(x)
square_root_2()
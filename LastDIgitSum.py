def LastDigitSum():
    prev = 0

    x = 0
    for x in range(0, 10):
        print ("Current number: ", x, " Previous number: ", prev, "Sum: " , prev+x)
        prev = x


LastDigitSum()
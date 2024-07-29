def BaseExp(base, exp):
    res = 1
    for i in range(0, exp):
        res *= base

    print(res)

BaseExp(2,5)

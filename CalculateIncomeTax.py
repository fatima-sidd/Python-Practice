def CalculateTax(value):


    t2 = 10/100
    t3 = 20/100
    
    if value > 20000:
        value -= 20000
        value = (value * t3) + (10000 * t2)

    elif value > 10000:
        value -= 10000
        value = value * t2

    print(value)

CalculateTax(45000)
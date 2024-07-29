def DivisibleByX(numbers, x):
    for i in numbers:
        if i % x == 0:
            print(i)


numbers = [10, 20, 33, 46, 55]

DivisibleByX(numbers, 5)

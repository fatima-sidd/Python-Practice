def ExtractReverse(number):
    string = str(number)
    length = len(string)

    for i in range(1, length + 1):
        print(string[-i], end=" ")
    print()

ExtractReverse(7536)
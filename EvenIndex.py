def PrintEven():
    originalString = "pynative"
    size = len(originalString)
    for i in range (0, size - 1, 2):
        print(originalString[i])

PrintEven()
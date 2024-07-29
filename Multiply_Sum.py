"""
Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
"""

def Product(num1, num2):
    return num1 * num2

def Sum(num1, num2):
    return num1 + num2

def ProductOrSum():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    product = Product(num1, num2)
    if product <= 1000:
        print("Product")
        return product
    
    else:
        print ("Sum")
        sum = Sum(num1, num2)
        return sum

print (ProductOrSum())
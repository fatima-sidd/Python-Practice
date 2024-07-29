"""
Given two list of numbers, write a program
 to create a new list such that the new list
 should contain odd numbers from the first list
 and even numbers from the second list.
"""

def JoinedList(list1, list2):
    resList = []

    for num in list1:
        if num % 2 != 0:
            resList.append(num)
    
    for num in list2:
        if num % 2 == 0:
            resList.append(num)

    print(resList)
    
l1 = [10, 20, 25, 30, 35]
l2 = [40, 45, 60, 75, 90]

JoinedList(l1, l2)
"""
Write a program to remove the item present
at index 4 and add it to the 2nd position
and at the end of the list
"""
def ListAddRemove(listInput):

    item = listInput.pop(4)
    print("List After removing element at index 4 ", listInput)

    listInput.insert(2, item)
    print("List after Adding element at index 2 ", listInput)

    listInput.append(item)
    print("List after Adding element at the end ", listInput)


list1 = [34, 54, 67, 89, 11, 43, 94]
ListAddRemove(list1)


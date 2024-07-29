def IsPalindrome(string):
    stringReverse = string[::-1]
    if string == stringReverse:
        print("True")
    else:
        print("False")

IsPalindrome("121")
IsPalindrome("125")
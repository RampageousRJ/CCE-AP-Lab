def palindromeCheck(str):
    if str==str[::-1]:
        return "Palindrome"
    return "Not Palindrome"
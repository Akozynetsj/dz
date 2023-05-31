def is_palindrome(string):
    string = string.replace(" ", "").lower()
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False
str1 = "А роза упала на лапу Азора"
print(f'Рядок "{str1}" є паліндромом: {is_palindrome(str1)}')
str2 = "Hello, World!"
print(f'Рядок "{str2}" є паліндромом: {is_palindrome(str2)}')


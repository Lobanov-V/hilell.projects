def is_palindrome(s: str) -> bool:
    clean=''.join(char.lower() for char in s if char.isalnum())
    return clean == clean[::-1]

s=(input("enter a string"))
print(is_palindrome(s))

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

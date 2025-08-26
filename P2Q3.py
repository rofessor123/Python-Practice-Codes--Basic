##check if string is palindrome 

##a palindrome is a word that reads the same forward and backward like Madam

def is_palindrome(text):
    # Remove spaces and convert to lowercase
    text = text.replace(" ", "").lower()
    
    # Compare string with its reverse
    #text[::-1] reverses the string
    return text == text[::-1] 

# Example
print(is_palindrome("madam"))   # True
print(is_palindrome("hello"))   # False

def is_palindrome(text):
    text.lower()
    reverse_text = text[::-1]

    if text == reverse_text:
        return True
    else:
        return False

text = input("Podaj tekst: ")
print(is_palindrome(text))
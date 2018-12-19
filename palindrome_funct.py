def palindrome(word):
    """Checks a word to see if it is the same in reverse."""
    word = word.lower()
    return word[::-1] == word

print(palindrome("dad"))
print(palindrome("python"))

def is_this_palindrome(word):
    y = len(word)
    z = 0
    backward = (word[::-1])
    if backward == word:
        print("This is palindrome!")
    else:
        print ("This is not palindrome!")

is_this_palindrome("kajak")

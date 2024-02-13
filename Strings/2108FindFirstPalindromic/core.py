def test(words):
    
    is_palindromic = lambda s: s == s[::-1]

    for word in words:
        if is_palindromic(word) == True:
            return word
    return ''
        

print(test(["abc","car","ada","racecar","cool"]))
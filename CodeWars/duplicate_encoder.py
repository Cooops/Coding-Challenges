# MY SOLUTION
def duplicate_encode(word):
    """(str) -> str

    Takes in a string and checks the number of occurences each letter has. If a letter occurs more than once, then change that value to ')', otherwise chane the value to '('.
    print((duplicate_encode("test"))) => ")(()"
    """
    word = word.lower()
    modWord = [letter.replace(letter, ')') if word.count(letter) > 1 else '(' for letter in word]
    return ''.join(modWord)
    
# TOP SOLUTION
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

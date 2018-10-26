# http://www.codewars.com/kata/your-order-please/train/python

"""
Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

your_order("is2 Thi1s T4est 3a")
[1] "Thi1s is2 3a T4est"
"""

# MY SOLUTION
import re

def order(sentence):
    stack = {}
    for word in sentence.split():
        for letter in word:
            if letter.isdigit():
                # after grabbing all of the digits, 
                # add key:values to a dict so we can easily sort the order
                # stack[re.sub(r'(\d+)', '', word)] = letter  # uncomment if we wanted to instead replace each of the digits
                stack[word] = letter
    # sort the dict by the using the .get method on our dict to force-sort by the values (digits)
    return ' '.join(sorted(stack, key=stack.get))

# TOP SOLUTION
def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

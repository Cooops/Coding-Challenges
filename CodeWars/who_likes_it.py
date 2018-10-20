# http://www.codewars.com/kata/who-likes-it/python

# MY SOLUTION
def likes(users):
    """ (str) => str
    
    Takes in a string and updates a new string with the number of users who liked it.
    """
    if len(users) == 0:
        return "no one likes this"
    elif len(users) == 1:
        return "{} likes this".format(users[0])
    elif len(users) == 2:
        return "{} and {} like this".format(users[0], users[1])
    elif len(users) == 3:
        return "{}, {} and {} like this".format(users[0], users[1], users[2])
    else:
        return "{}, {} and {} others like this".format(users[0], users[1], len(users)-2)

# TOP SOLUTION
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

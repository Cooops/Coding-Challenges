# https://www.codewars.com/kata/57fa9bc99610ce206f000330

"""
Pete and his mate Phil are out in the countryside shooting clay pigeons with a shotgun - amazing fun.

They decide to have a competition. 3 rounds, 2 shots each. Winner is the one with the most hits.

Some of the clays have something attached to create lots of smoke when hit, guarenteed by the packaging to generate 'real excitement!' (genuinely this happened). None of the explosive things actually worked, but for this kata lets say they did.

For each round you will receive the following format:

[{P1:'XX', P2:'XO'}, true]

That is an array containing an object and a boolean. Pl represents Pete, P2 represents Phil. X represents a hit and O represents a miss. If the boolean is true, any hit is worth 2. If it is false, any hit is worth 1.

Find out who won. If it's Pete, return 'Pete Wins!'. If it is Phil, return 'Phil Wins!'. If the scores are equal, return 'Draw!'.

Note that as there are three rounds, the actual input (x) will look something like this:

[[{P1:'XX', P2:'XO'}, true], [{P1:'OX', P2:'OO'}, false], [{P1:'XX', P2:'OX'}, true]]
"""

# MY SOLUTION
def shoot(results):
    resultsLen = len(results)
    score = {}
    if resultsLen > 1:
        for game in range(0, len(results)):
            playerDict = results[game][0]
            boolCheck = results[game][1]
            pete = playerDict['P1']
            phil = playerDict['P2'] 
            if not score:
                if boolCheck == True:
                    score['Pete'] = pete.count('X')*2
                    score['Phil'] = phil.count('X')*2
                else:
                    score['Pete'] = pete.count('X')
                    score['Phil'] = phil.count('X')
            else:
                if boolCheck == True:
                    score['Pete'] += pete.count('X')*2
                    score['Phil'] += phil.count('X')*2
                else:
                    score['Pete'] += pete.count('X')
                    score['Phil'] += phil.count('X')
    return 'Pete Wins!' if score['Pete'] > score['Phil'] else 'Draw!' if score['Pete'] == score['Phil'] else 'Phil Wins!'

# TOP SOLUTION
def shoot(results):
    p1_score = 0
    p2_score = 0
    
    for round in results:
        if round[1]:
            inc = 2
        else:
            inc = 1
        
        p1_shoots = round[0]['P1']
        p2_shoots = round[0]['P2']
        
        for shoot in p1_shoots:
            if shoot == 'X':
                p1_score += inc
                
        for shoot in p2_shoots:
            if shoot == 'X':
                p2_score += inc
    
    if p1_score > p2_score:
        return 'Pete Wins!'
    elif p1_score < p2_score:
        return 'Phil Wins!'
    else:
        return 'Draw!'

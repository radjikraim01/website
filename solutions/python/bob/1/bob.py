"""
this was too hectic to solve for my liking 
"""
def response(hey_bob):
    """
    same not clean road to reach the solution
    """
    hey_bob=hey_bob.strip()
    if len(hey_bob)==0:
        return "Fine. Be that way!"
    if hey_bob[-1]=="?" and hey_bob.upper()==hey_bob and any(c.isalpha() for c in hey_bob):
        return "Calm down, I know what I'm doing!"
    if hey_bob.upper()==hey_bob and hey_bob[-1]!="?" and any(c.isalpha() for c in hey_bob):
        return "Whoa, chill out!"
    if hey_bob[-1]=="?":
        return "Sure."
    return "Whatever."
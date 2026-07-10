"""
debugging issues is still my weak spot in code
"""
def factors(value):
    """
    completlyy missed the second needed if haaaaayaaaaaaaa
    """
    prime=[]
    counter=2
    while value>1:
        if value%counter==0:
            value=value/counter
            prime.append(counter)
        if value%counter!=0:
            counter+=1
    return prime
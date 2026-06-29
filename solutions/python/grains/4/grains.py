"""
this reminds me of the chinese quiz of a guy acting smart asking for a rice that doubles each something something
"""
def square_but_with_full_list(number):
    """
    made this because i needed list for total and i thought this way it would be cleaner then clutering total function this one is added on my own the exercice only asked for 2
    this one got me the most errors because i really forgot that i left a try block at the top and kept hitting error messages 
    """
    value_end=[1]
    count=1
    while count<number:
        value_end.append(value_end[-1]*2)
        count+=1
    return value_end
def square(number):
    """
    output on this one should be the last item value number this one was easy to spot in tests but it is tricky for a bit
    """
    if number>64 or number<=0:
        raise ValueError("square must be between 1 and 64")
        
    value_end=[1]
    count=1
    while count<number:
        value_end.append(value_end[-1]*2)
        count+=1
    return value_end[-1]

def total():
    """
    at first i thought i can use square on this one but the issue is that i kept getting int is not itteratable so since it is night by the time iw as doing this dumb me thought it was the code that is wrong hahahahaha ended up needing to create a new function which i could have done somethings to square and avoide that but ehh it is a bit i feel 
    """
    return sum(square_but_with_full_list(64))
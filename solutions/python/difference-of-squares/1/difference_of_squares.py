"""
i do not know what to say about this one
"""
def square_of_sum(number):
    """
    it is a simple counter i could have done it a cleaner way but why bother
    """
    counter=1
    value=0
    while counter<number+1:
        value+=counter
        counter+=1
    return value*value


def sum_of_squares(number):
    """
    this one is even simpler to make just copy the first with small modifications
    """
    counter=1
    value=0
    while counter<number+1:
        value+=counter*counter
        counter+=1
    return value 


def difference_of_squares(number):
    """
    this is done i think like i said in the start this could have been done in a way cleaner way but why bother
    """
    return square_of_sum(number)-sum_of_squares(number)

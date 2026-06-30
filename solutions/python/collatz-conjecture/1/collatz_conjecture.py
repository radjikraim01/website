"""
this one was simple overall i guess need to ask about how raise work tho
"""
def is_valid(number):
    """
    validation added it on my own like always reduce the cluter a bit i guess
    """
    if number<=0:
        raise ValueError("Only positive integers are allowed")
def steps(number):
    """
    really have nothing to say about this one to be honest
    """
    is_valid(number)
    number_list=[number]
    while number_list[-1]!=1:
        number_calc=number_list[-1]
        if number_calc%2==0:
            number_calc=number_calc/2
            number_list.append(number_calc)
        else:
            number_calc=(number_calc*3)+1
            number_list.append(number_calc)
    return len(number_list)-1
    

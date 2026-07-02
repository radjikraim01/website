"""
to be honest i could have done this cleaner but when making the solution i though thte input by the test is going to be string so i coded with that in mind by the time it failed the code was already in place so i just added a converion that is redunedat in lenght but i am just too ubothered to find an another solution at this point
"""
def is_armstrong_number(number):
    """
    i alread said everything i think in the above doc string nothing to add more here
    """
    number=str(number)
    list_number=list(number)
    power=len(list_number)
    sums=0
    for num in list_number:
        sums=sums+int(num)**power
    return sums==int(number)
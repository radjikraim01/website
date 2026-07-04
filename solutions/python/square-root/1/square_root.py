"""
i used The Newton-Raphson Formula had to websearch it since i have been a while since i did pure math and i am not sure if this is against the spirit of the test to be honest 
"""
def square_root(number):
    """
    i end up saying everything i want to say in the start that i do not have anything to type here
    """
    current=1
    while current*current!=number:
        current=0.5*(current+(number/current))
    return current
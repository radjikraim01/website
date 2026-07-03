"""
had help from turi for the math since fuck me but i hate math 
"""
def score(x_axis, y_axis):
    """
    ehh not sure hwo to feel about this one felt it was more math related then code 
    """
    distance =x_axis**2+y_axis**2
    if distance<=1:
        return 10
    elif distance<=25:
        return 5
    elif distance <=100:
        return 1
    return 0

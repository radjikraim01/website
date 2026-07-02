"""
what type of triangle it is code i added triangle is it on my own instead of making a new one at each function call and verifying if it is a trainagle to begin with i should also move the 0 check to ther too update added it just now
"""
def triangle_is_it(sides):
    """
    my own addition to the code function to test is it a valid traingle not bullet proof but should be enough for this one
    """
    if 0 in sides or len(sides)<3:
        return False
    sidea=sides[0]
    sideb=sides[1]
    sidec=sides[2]
    return sidea + sideb > sidec and sideb + sidec > sidea and sidea + sidec > sideb
def equilateral(sides):
    """
    is it equilateral
    """
    if not triangle_is_it(sides):
        return False
    return sides[0]==sides[1]==sides[2]

def isosceles(sides):
    """
    is it isosceles
    """
    if not triangle_is_it(sides):
        return False
    return sides[0]==sides[1] or sides[1]==sides[2] or sides[0]==sides[2]
        


def scalene(sides):
    """
    is it scalene
    """
    if not triangle_is_it(sides):
        return False
    return sides[0]!=sides[1] and sides[1]!=sides[2] and sides[0]!=sides[2]
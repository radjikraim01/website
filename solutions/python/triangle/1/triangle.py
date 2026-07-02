def triangle_is_it(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    return a + b >= c and b + c >= a and a + c >= b
def equilateral(sides):
    if triangle_is_it(sides)==False:
        return False
    if 0 in sides or len(sides)>3:
        return False
    return sides[0]==sides[1]==sides[2]

def isosceles(sides):
    if triangle_is_it(sides)==False:
        return False
    if 0 in sides or len(sides)>3:
        return False
    return sides[0]==sides[1] or sides[1]==sides[2] or sides[0]==sides[2]
        


def scalene(sides):
    if triangle_is_it(sides)==False:
        return False
    if 0 in sides or len(sides)>3:
        return False
    return sides[0]!=sides[1] and sides[1]!=sides[2] and sides[0]!=sides[2]


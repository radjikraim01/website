"""
did a dumb mistake on this one at the start since most exercices ask fro return i returned all of them togheter like a dumb dum the end list one is just me being clever i could have solved it too with print but print that just have sep="" and end="" so it is just that way anyway i might be wrong about this solution here that i proposed just now but the one i made is good to go it is the same as fizz buzz in leet code
"""
def convert(number):
    """
    i feel solution is not optimal reallly with this one it should not be bad by itself but i could maybe right it in a way to reduce code lines maybe i could have made it a tuple unpacked to the chcick for sound anyway 
    """
    result=[]
    if number%3==0 or number%5==0 or number%7==0:    
        if number%3==0:
            result.append("Pling")
        if number%5==0:
            result.append("Plang")
        if number%7==0:
            result.append("Plong")
    else:
        result.append(str(number))
    return "".join(result)

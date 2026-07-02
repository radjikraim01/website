"""
not clean solution at all it is very bad not sure what happen to me when i am thinking about something time space related this si not time related but it is space related
"""
def clean(isbn):
    """
    not clean
    """
    return [char for char in isbn if char.isdigit() or char == 'X']
def validation(isbn):
    """
    hate that i had to add so many checks like this to return a false wait a min maybe can fix oha made the check a long ass one liner but it is no good still  
    """
    alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']
    return not(len(isbn)!=10 or len(isbn) is None or "X" in isbn[:-1] or isbn is None or isbn[-1] in alphabet)
        
def is_valid(isbn):
    """
    i feel this is the most unclean code i have wrote in a while and i was very bad not long ago but god damn it is looking ass like this 
    """
    if len(isbn)==0:
        return False
    isbn=isbn.replace("-","")
    if validation(isbn)==False:
        return False
    isbn=list(isbn)
    if validation(isbn)==False:
        return False
    isbn=clean(isbn)
    if validation(isbn)==False:
        return False
    for iteration in range(len(isbn)):
        if isbn[iteration]=="X":
            isbn[iteration]=10
    var=0
    counter=0
    valid=10
    while counter<10:
        var+=int(isbn[counter])*valid
        counter+=1
        valid-=1
    return var%11==0
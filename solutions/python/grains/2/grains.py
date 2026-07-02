def square_but_with_full_list(number):
    value_end=[1]
    for value in range(1,number):
        value_end.append(value_end[-1]*2)
    return value_end
def square(number):
    if number>64 or number<=0:
        raise ValueError("square must be between 1 and 64")
        
    value_end=[1]
    count=1
    while count<number:
        value_end.append(value_end[-1]*2)
        count+=1
    return value_end[-1]

def total():
    return sum(square_but_with_full_list(64))
"""
it is hell to go through this one it is finllay over do not even have anything to say about it but just do not code math problems when sleepy everything is 10 times harder for no nreason
"""
def is_valid(input_base,digits,output_base):
    """
    validation on my own like always
    """
    if input_base<2:
        raise ValueError("input base must be >= 2")
    if output_base<2:
        raise ValueError("output base must be >= 2")
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
def get_number(input_base,digits):
    """
    sperated this so if the issue stems from here the fixing would be easier 
    """
    counter=0
    power=len(digits)-1
    number=0
    while counter <len(digits):
        number+=digits[counter]*(input_base**power)
        counter+=1
        power-=1
    return number
def out_number(number, output_base):
    """
    same reason for the above
    """
    number_out=[]
    while number!=0:
        number_out.append(number%output_base)
        number=number//output_base
    return number_out[::-1]
def rebase(input_base, digits, output_base):
    """
    this was hectic and that is all i can say about this one 
    """
    is_valid(input_base,digits,output_base)
    if sum(digits)==0:
        return [0]
    number=get_number(input_base,digits)
    number_out=out_number(number,output_base)
    return number_out
    
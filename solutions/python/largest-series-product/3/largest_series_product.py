"""
this is a largest s3eries product exercie i swear i think i solved this in leet code
"""
def is_valid(series,size):
    """
    exeerciec did nto ask fro this i addedd it to not make the main function bigger
    """
    if size==0:
        raise ValueError("the size must not be 0")
    if size>len(series):
        raise ValueError("span must not exceed string length")
    if size<0:
        raise ValueError("span must not be negative")
    if any(piece.isalpha() for piece in series):
        raise ValueError("digits input must only contain digits")
def largest_product(series, size):
    """
    maine exercice core not really much to say about it really
    """
    is_valid(series, size)
    product_max=0
    series=list(series)
    left=0
    right=size+left
    while right<=len(series):
        product=1
        for number in series[left:right]:
            product*=int(number)
        product_max=max(product_max,product)
        left+=1
        right+=1
    return product_max
    
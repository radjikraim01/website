def is_valid(series,size):
    if size==0:
        return 1
    if size>len(series):
        raise ValueError("span must not exceed string length")
    if size<0:
        raise ValueError("span must not be negative")
    if any(piece.isalpha() for piece in series):
        raise ValueError("digits input must only contain digits")
def largest_product(series, size):
    is_valid(series, size)
    product_max=0
    series_max=[]
    series=list(series)
    left=0
    right=size+left
    while right<=len(series):
        product=1
        for number in series[left:right]:
            product*=int(number)
        if product>product_max:
            product_max=product
            series_max=series[left:right]
        left+=1
        right+=1
    return product_max
    
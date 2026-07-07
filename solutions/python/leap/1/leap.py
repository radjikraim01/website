"""
the year 100 part was tricky when tired because i read 4 firs then i instead of relating 100 to both of 4 and 400 i only linked it to 400 divsion part
"""
def leap_year(year):
    """
    i think tho i have seen this in leet code i think no ? to be honest i am not sure Also this is for you turi
    """
    return (year%4==0 and year%100!=0) or (year%100==0 and year%400==0)

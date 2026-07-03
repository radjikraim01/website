"""
i am trying to one shot this if this text still apears then the attempt was one shotted this one was weird to be honest i failed because i forgot to clean lower and add a safe guard for none so it was a 3rd attempt that all of them are just about cleaning so it is not a one shot as i hoped 
"""
def cleaning(sentence):
    """
    used this in another code copied it direclty since it is just as relvent here 
    """
    sentence_cleaned=[]
    for char in sentence:
        if char.isalpha():
            sentence_cleaned.append(char)
    sentence_cleaned="".join(sentence_cleaned)
    return sentence_cleaned
def is_isogram(phrase):
    """
    this one is a bit easier i think hopefully nothing breaks but it should be good to go 
    """
    if len(phrase)==0:
        return True
    phrase=phrase.lower()
    phrase=cleaning(phrase)
    return len(phrase)==len(set(phrase))
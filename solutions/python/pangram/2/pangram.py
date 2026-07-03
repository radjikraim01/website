"""
had to websearch the isalpha method but otherwise this was a clean build 
"""
def cleaning(sentence):
    """
    this was added by me to clean input in i am not sure if i covered all edge cases but it should be good to go otherwise i hope
    """
    sentence_cleaned=[]
    for char in sentence:
        if char.isalpha():
            sentence_cleaned.append(char)
    sentence_cleaned="".join(sentence_cleaned)
    return sentence_cleaned
def is_pangram(sentence):
    """
    this one too is clean i can fix it a bit more but i am not sure if it would be worth it if i do more here to it 
    """
    if len(sentence)==0:
        return False
    sentence=sentence.lower()
    sentence=cleaning(sentence)
    sentence=list(sentence)
    sentence=set(sentence)
    return len(sentence)==26
def get_words(text):
    wc = text.split()
    w = len(wc)
    return w
def get_num_letters(text):
    letter = {}
    tx = text.lower()
    for i in tx:
        if i not in letter:
            letter[i]=1
        else:
            letter[i]+=1
    return letter
    
    
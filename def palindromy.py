
s=input('Wpisz słowo= ')

def pali(s):
    if len(s)==0:
        return True
    elif len(s)==1:
        return True

    if s[0]==s[-1]:
        return pali(s[1:-1])
    else:
        return False
    
print(pali(s))

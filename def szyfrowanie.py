n=int(input('wpisz ilosc= '))

def thue(a,b,n):
    if n==1:
        return a
    if n==2:
        return a+b

    else:
        return thue(a,b,n-1)+thue(b,a,n-1)

print(thue('a','b',n))

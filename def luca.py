n=int(input('Podaj liczbę n= '))

def luca(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return luca(n-1)+ luca(n-2)

print('Wynik = ',luca(n))
        

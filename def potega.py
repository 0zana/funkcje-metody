a=int(input('Liczba, która zostanie podniesiona do potęgi= '))
n=int(input('Potęga= '))
def potega(a, n):
    if n==0:
        return 1

    else:
        return a*potega(a, n-1)

print('Wynik potęgowania: ', potega(a,n))
        

n=int(input('Liczba= '))

def suma(n):
    if n==1:
        return 1

    else:
        return n+suma(n-1)

print('Wynik= ', suma(n))

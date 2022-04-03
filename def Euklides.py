#sprawdzenie, jaki jest największy wspólny dzielnik dwóch liczb

def Euklides(pierwsza, druga):
    while pierwsza!=druga:
        if pierwsza>druga:
            pierwsza=pierwsza-druga
            return(Euklides(pierwsza,druga))
        else:
            druga=druga-pierwsza
            return(Euklides(druga,pierwsza))
    return(pierwsza)

i=0
while i==0:
    pierwsza=int(input("wpisz pierwszą liczbę = "))
    druga=int(input("wpisz drugą liczbę = "))
    print(Euklides(pierwsza,druga))
    ask=input("czy chcesz sprawdzić następne liczby? (true/false) ")
    if ask=="false":
        i+=1


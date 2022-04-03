#sprawdzanie, czy liczba jest doskonała, czyli czy suma jej dzielników właściwych jest jej równa

def doskonala(a):
    i=2
    czyDoskonala=1

    while i<a:

        if a%i==0:
            czyDoskonala=czyDoskonala+i
        i=i+1

    if czyDoskonala==a:
        return True

    else:
        print(a, " nie jest liczbą doskonałą, bo suma jej dzielników = ", czyDoskonala)

i=0
while i==0:
    liczba=int(input("wpisz liczbę i sprawdź czy jest doskonała "))
    print(doskonala(liczba))
    ask=input("chcesz sprawdzić kolejną liczbę? (true/false) ")
    if ask!="true":
        i=i+1
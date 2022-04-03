n=int(input('Wpisz liczbę kółek= '))

A=[]
B=[]
C=[]
u=n
A.append(n)

while u>1:
    A.append(u-1)
    u=u-1

def hanoi(A,B,C,n):
    
    if n==1:
        C.append(A.pop())
        
    else:
        hanoi(A,C,B,n-1)
        print(A,B,C)
        
        C.append(A.pop())
        print(A,B,C)
        
        hanoi(B,A,C,n-1)
        print(A,B,C)

hanoi(A,B,C,n)

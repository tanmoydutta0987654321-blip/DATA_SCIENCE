def letter():
    x=input("Enter your String :")
    y=input(f"Enter what is you remove from {x}:")
    X=x.upper()
    Y=y.upper()
    if Y in X:
         L1=list(X)
         L1.remove(Y)
         print(L1)
    else:
         print("enter y from  x not other")
# letter()

def evlen():
    x=input("Enter Your String:").upper()
    word=x.split()
    for i in word:
        if len(i) %2 ==0:
            print(i)
        else:
            print("No")
# evlen()

def uphalf():
    x=input("Enter a String :")
    if len(x)%2==0:
        s=x.split()
        print(s)
        for i in s:
           print(i)
uphalf()

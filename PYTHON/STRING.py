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
    print(word)
    for i in word:
        if len(i) %2 ==0:
            print(i)
        else:
            print("No")
evlen()
print("-----------------------------------------")

# def even_length_words():
#     text = input("Enter your string: ")
#     words = text.split()   # split into words by spaces
    
#     print("Even-length words are:")
#     for word in words:
#         if len(word) % 2 == 0:   # check if length is even
#             print(word)

# even_length_words()

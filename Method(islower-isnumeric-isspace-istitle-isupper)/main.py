# islower and its type
st1 = input("Enter a string :")    # OUTPUT:1- Enter a string :krinshna
st1 = st1.islower()                # True <class 'bool'>
print(st1, type(st1))              # 2- Enter a string :MOHIni
                                   # Flase <class 'bool'>
# isnumeric and its type
st2 = input("Enter a string :")    # Output:1-Enter a string : 123456
st2 = st2.isnumeric()              # True <class 'bool'>
print(st2, type(st2))              # 2-Enter a string : krishna
                                   # Flase <class 'bool'>
# isspace and its type
st3 = input("Enter a string :")
st3 = st3.isspace()
print(st3, type(st3))

# istitle and its type
st4 = input("Enter a string :")
print(st4.istitle(), type(st4))

# isupper and its type
st5 = input("Enter a string :")   # OUTPUT:Enter a string : Mohini
st5 = st5.isupper()               # False <class 'bool'>
print(st5, type(st5))

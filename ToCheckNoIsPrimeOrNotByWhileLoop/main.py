#To check number is prime or not by while loop and not using third element
N = int(input("Enter a number to check :"))
I = N-1
if N < 2:
    print("Number is not prime")
else:
    while I > 1:
        if N % I == 0:
           print("Number is not prime")
           break
        I -= 1
    else:
        print("Number is prime")



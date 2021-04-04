#To check number is prime or not without using third element
N = int(input("Enter a number :"))
if N < 2:
    print("Number is not prime ")
else:
    for i in range(2, N):
        if N % i == 0:
            print("Number is not prime ")
            break
    else:
        print("Number is  prime")

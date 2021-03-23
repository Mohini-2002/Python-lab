N = int(input("Enter a number :"))
rev = 0
while N > 0:
    rem = N % 10
    rev = (rev*10)+rem
    N = N//10
print(rev)
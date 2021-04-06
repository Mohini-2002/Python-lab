#To print the N number of table:
N = int(input("Enter the limit of table :"))
a = 1
while a <= N:
    i = 1
    while i <= 10:
        t = i*a
        print(t, end="  ")
        i += 1
    print("\n")
    a += 1

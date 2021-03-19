N = int(input("Enter the length :"))
for i in range(1, N+1):
    if i % 5 == 0 and i % 10 != 0:
        print(i)


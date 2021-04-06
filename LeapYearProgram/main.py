#TO CHECK GIVEN YEAR IS LEAP YEAR OR NOT
Year = int(input("Enter a year to check :"))
if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("Given year is leap year")
        else:
            print("Given year is not a leap year")
    else:
        print("Given year is leap year")
else:
    print("Given year is not a leap year")

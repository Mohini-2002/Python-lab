#Capitalize (capital the first of a string and its type print)
ST1 = input("Enter a string :")
ST1 = ST1.capitalize()
print("After capitalize use : ", ST1, type(ST1))

#Center (fill the free space of a string and and its type print)
ST2 = input("ENter a string :")
ST2 = ST2.center(20, "#")
print("After center use :", ST2, type(ST2))
#Count (Count the st occurs in string and its type print)

ST3 = input("Enter a string :")
ST3 = ST3.count('O', 1, 10)
print(ST3, type(ST3))

#Encode
ST4 = input("Enter a string : ")
ST4 = ST4.encode("utf-8")
print(ST4, type(ST4))

#Decode
ST5 = input("Enter a string :")
ST5 = ST5.decode(encoding="UTF-8", erros='strict')
print(ST5, type(ST5))
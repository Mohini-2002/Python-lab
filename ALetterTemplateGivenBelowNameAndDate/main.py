#Write a program to fill in a letter template given below with name and date
name = input("Enter a name :")
date = input("Enter the date :")
letter = '''Dear <|NAME|>,
Our company(The name of company is MOON) is  very happy to tell you
that your are selected for our company.
And you can join our company  for 
a best experience !!!  
Thank you..... 
Date:<|DATE|>'''
letter = letter.replace("<|NAME|>",  name)
letter = letter.replace("<|DATE|>", date)
print(letter)
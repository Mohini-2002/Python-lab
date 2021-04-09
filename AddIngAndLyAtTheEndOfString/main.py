#Add 'ing' at the end of a given string(length should be at least 3).If the given string already end with 'ing'
#Then add 'ly' instead.If the length of string is less then 3 then strig should be unchanged.
st = input("Enter a string :")
d = len(st)
if d >= 3:
   re = st.endswith("ing")
   if re == True:
      print(st+"ly")
   else:
       print(st+"ing")
else:
    print("String should not change")

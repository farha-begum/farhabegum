char=input("enter a single character:")
if len(char)!=1:
    print("enter one character!")
else:
     if char.isdigit():
                       print(f"'{char}' is a digit.")
     elif char.lower():
                       print(f"'{char}' is a lowercase character.")
     elif char.isupper():
                         print(f"'{char}' is a uppercase character.")
     else:
         print(f"'{char}' is a special character.")
                              

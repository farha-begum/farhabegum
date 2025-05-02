char=input("enter a single character:")
if len(char)!=1:
    print("please enter only one character!")
    else:
    
    if char.isdigit():
            print(f"'{char}'is a digit.")
            elif char.islower():
                print(f"'{char}' is a lower case character.")
                elif char.isupper():
                    print("'{char}' is a upper case character.")
                    else:
                        print(f"'{char}' is a specuial case character.")
                        

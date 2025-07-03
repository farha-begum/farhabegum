n_terms=int(input("enter the number of fibonacciu terms to display:"))
a,b=0,1
count=0
if n_terms<=0:
    print("please enter a positive integer:")
elif n_terms==1:
    print("fibonacci sequence:")
    print(a)
else:
     print("fibonacci sequence:")
     while count<n_terms:
         print(a,end="")
         a,b=b,a+b
         count+=1

principal=int(input("enter principal amount"))
rate=float(input("enter rate of interest"))
time=int(input("enter period"))
amount=principal*(pow((1+rate/100),time))
ci=amount-principal
print(("compound interestis:",ci))
       


def gcd(a,b):
    """
   computethe greatest common divisor(GCD) of two numbers using the euclidean algorithm
   :param a:first number(integer).
   :param b:second number(integer).
   :return:GCD of a and b.
   """
    while b!=0:
          a,b=b,a%b
    return a
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

result=gcd(num1,num2)
print(f"the gcd of {num1} and {num2} is :{result}")

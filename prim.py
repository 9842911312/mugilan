a=int(input("enter the number"))

k=0

if a==0:

    print("print valid number")

else:

    for i in range(2,a//2+1):

        if(a%i==0):

            k = k + 1

if(k<=0):

    print("number is prime")

else:

     print("number is notprime"

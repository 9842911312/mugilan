x=int(input("enter the number"))

temp=x

res=0

while(x>0):
 
    dig=x%10

    res=res*10+dig

    x=x//10

if(temp==res):

    print("it is palindorm")

else:

    print("it is palindorm")

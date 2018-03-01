r=int(input("enter upper limit:"))
for a in range(2,r+1):
  k=01
 for i in range(2,a//2+1):
    if(a%i==0):
     k=k+1

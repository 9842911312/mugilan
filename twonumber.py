n=int(input("enter the number"))

k=int(input("enter the number"))

ll=[]

s=0

for i in range(0,n):

    a=input()

    ll.append(a)

for i in range(0,k):

    s=s+int(ll[i])

print(s)    

x=0
y=1
p=0
n=int(input("enter"))
if n==0:
    print(0)
while p<n:
    p=p+1
    z=x+y
    print (z)
    x,y=y,z

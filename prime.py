x=int(input("Enter a number: "))
flag=0
for i in range(2,x-1):
    if(x%i==0):
        flag=1
        break
if(x==1):
    print("Neither prime nor composite")
elif(flag==1):
    print("The number is not prime")
else:
    print("The number is prime")

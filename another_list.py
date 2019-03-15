a=[]
n=int(input("How many numbers u wanna enter??: "))
for i in range(n):
    op=input("Do you want to enter a sublist?  yes or no: ")
    if(op=="yes"):
        sub_l=list(input("Enter value: ").split(" "))
        a.append(sub_l)
    else:
        a.append(input("Enter value: "))
print(a)
try:
   ind=int(input("Enter the index at which you wanna perform deletion: "))
   print("Enter the value u wanna delete: ",a[ind])
   l=a[ind]
   val=input()
   l.remove(val)
   print(a)
except:
    print("Wrong input")


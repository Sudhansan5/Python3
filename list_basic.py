a=[]
n=int(input("How many numbers you want to enter: "))
for i in range(n):
    op=input("Do you want to enter sub-list __Enter yes or no: ")
    if(op=='yes'):
        sub_l=list(input("Enter list values: ").split(" "))
        a.append(sub_l)
    else:
        a.append(int(input("Enter value: ")))
ind=int(input("Enter index of inner list at which you want to perform deletion: "))
print(a[ind])
jak = input("What value you want to delete")













a[ind].remove(jak)
print(a)


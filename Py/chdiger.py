t=int(input())
while(t>0):
    flag=0;a=[]
    n,d=map(str,input().split())
    for i in n:
        a.append(i)
    if(a[len(n)-1]>d):
        a[len(n)-1]=d
    for i in range(len(n)-2,-1,-1):
        if(a[i]>a[i+1]):
            a.pop(i)
            a.append(d)
    for i in a:
        print(i,end="")
    print("")
    t-=1
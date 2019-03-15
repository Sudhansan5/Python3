t=int(input())
while(t>0):
    n=int(input())
    max=0
    a=list(map(int,input().split()))
    d=list(map(int,input().split()))
    if(d[0]-(a[n-1]+a[1])>0):
        max=d[0]
    for i in range(1,n-1):
        temp=d[i]-(a[i-1]+a[i+1])
        if(0<temp and d[i]>max):
                max=d[i]
    temp=d[n-1]-(a[n-2]+a[0])
    if(temp>0 and temp>max):
        max=temp
    print(temp)
    t-=1
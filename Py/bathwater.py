t=int(input())
while(t>0):
    v1,t1,v2,t2,v3,t3=map(int,input().split())
    if(t1==t3 and v1>=v3):
        print("YES")
    elif(t2==t3 and v2>=v3):
        print("YES")
    elif(t3>t2):
        print("NO")
    else:
        v1temp=(v2*(t2-t3))/(t3-t1)
        v2temp = (v1 * (t1 - t3)) / (t3 - t2)
        if(v1temp+v2>=v3):
            print("YES")
        elif (v2temp+v1 >= v3):
            print("YES")
        else:
            print("NO")
    t-=1
#hey prabhu
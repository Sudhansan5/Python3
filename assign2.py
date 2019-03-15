name = []
bg=[]
city=[]
n=1
while(n==1):
  n=int(input("Choose\n1.Enter data\n2.Exit\n"))
  if(n==1):
    name.append(input("Enter name: "))
    bg.append(input("Enter blood group: "))
    city.append(input("Enter city name: "))
for i in range(len(name)):
             for j in range(len(name)):
               if (bg[i]==bg[j]and city[i]==city[j] and i!=j):
                   print(name[j],bg[j],city[j])
        
            
            

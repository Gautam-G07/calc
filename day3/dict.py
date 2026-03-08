stud={}
for i in range(3):
    x=input("enter subject")
    y=int(input("enter marks"))
    stud[x]=y
for key,value in stud.items():
    print(key,value)    
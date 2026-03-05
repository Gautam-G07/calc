numbers=[]
x=int(input("Enter total nos"))
for i in range(x):
    y=int(input("enter no"))
    numbers.append(y)
max=numbers[0]
l2=[]
sum=0
c=0
for i in numbers:
    print(i)
    sum=sum+i
    if i>max:
        max=i
    if i%2==0:
        c=c+1
    if i>10:
        l2.append(i)
    else:
        continue
print("the list is",numbers)        
print("the sum is",sum)
print("biggest no is",max)
print("count of even numbers is",c)
print("nos greater than 10 are")
print(l2)
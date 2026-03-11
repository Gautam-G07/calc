class student:
    students=[]
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
        student.students.append(self)
    def display(self):
        print("Name:",self.name,"Age:",self.age,"Marks:",self.marks,"\n")
    @classmethod
    def showall(cls):
        if len(cls.students)==0:
            print("no students")
            return
        for s in cls.students:
            s.display()
    @classmethod
    def highest(cls):
        high=cls.students[0]
        if len(cls.students)==0:
            print("no students")
            return
 
        for i in cls.students:
            if i.marks>high.marks:
                high=i
        for s in cls.students:
            s.display()
        print("Highest no is",high)
                
    @classmethod
    def average(cls):
        sum=0
        if len(cls.students)==0:
            print("no students")
            return
        for i in cls.students:
            sum=sum+i.marks
        avg=sum/len(cls.students)
        print("the average is",avg)
while True:
    print("\n1.Add Student")
    print("\n2.Show Students")
    print("\n3.Find Highest")
    print("\n4.Find Average")
    print("\n5.Exit")
    choice=int(input("enter choice"))
    if choice==1:
        name=input("Enter name")
        age=int(input("Enter age"))
        Marks=int(input("Enter marks"))
        student(name,age,Marks)
    elif choice==2:
        student.showall()
    elif choice==3:
        student.highest()
    elif choice==4:
        student.average()
    elif choice==5:
        break
    else:
        print("Invalid choice")

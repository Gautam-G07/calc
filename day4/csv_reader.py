import csv

with open("day4/students.csv","a",newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Gautam","19","99"]) 

with open("day4/students.csv","r",newline='') as file:
    read = csv.reader(file)

    mark = 0
    high = ''

    for i in read:
        if len(i) < 3:
            continue

        name = i[0]
        age = i[1]

        try:
            marks = int(i[2])
        except ValueError:
            continue

        print(name, marks)

        if marks > mark:
            mark = marks
            high = name

print("the student with the highest marks is", high, "and highest marks is", mark)
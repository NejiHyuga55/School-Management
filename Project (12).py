import csv
def add_student(file_name,name,class_,rollno,marks):
    with open(file_name,'a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([name,class_,rollno,*marks])
def display_student():
    with open("student.csv","r") as file:
        reader=csv.reader(file)
        for row in reader:
            name,class_name,roll_no,*marks=row
            marks=list(map(float,marks))
            average_marks=sum(marks)/len(marks)
            print(f"Name:{name}\nClass:{class_name}\nRoll No:{roll_no}")
            print("Marks:",','.join(map(str,marks)))
            print(f"Average Marks:{average_marks:.2f}\n{'='*20}")
def delete_student(roll_no):
    records=[]
    with open("student.csv",'r') as file:
        reader=csv.reader(file)
        for row in reader:
            if row[2]!=roll_no:
                records.append(row)
    with open("student.csv",'w',newline='')as file:
        writer=csv.writer(file)
        writer.writerows(records)
        print("student record deleted successfully")
def main():
    file_name='student.csv'
    while True:
        print("1. Add Student Record\n2. Display Student Records\n3. Delete Student Record\n4. Exit")
        choice=input("enter your choice:")
        if choice =='1':
            name = input("Enter Student Name:")
            class_=input("Enter Class:")
            rollno=input("Enter RollNo:")
            marks=[int(input(f"Enter Marks In {subject}:")) for subject in ['English','Maths','Physics','Chemistry','Computer']]
            add_student(file_name,name,class_,rollno,marks)
            print("Student Record Added Successfully")
        elif choice == '2':
            display_student()
        elif choice== '3':
            S= input(" Enter RollNo Of Student To Delete:")# here S is the roll no of a student to delete
            print(delete_student(5))
        elif choice=='4':
            print("Exiting...")
            break
        else:
            print("invalid choice!")
main()

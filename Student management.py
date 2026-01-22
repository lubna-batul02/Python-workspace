def show_menu():
    print("____Student Management System____")
    print("1. Add Student")
    print("2. View All Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    
students=[]
def add_stud_details():
    while True:
        try:
            Name = input("Enter student Name: ").strip()
            if Name.isalpha():
                break
            else:
                print("Enter only alphabets")
        except:
            print("Something went wrong with Name input")
            
    while True:
        try:
            ID=int(input("Enter student ID: "))
            break
        except:
            print("Enter only Integers")
            
    while True:
        try:
            Age= int(input("Enter student Age: "))
            break
        except:
            print("Enter valid number for Age")
            
        
    available_courses = ["BCA", "BSC", "BCOM", "BA", "MCA"]
    while True: 
        try:
            print("Available Courses:", ", ".join(available_courses))
            Course=input("Enter student Course: ")
            if Course in available_courses:
                break
            else:
                print("Invalid course! Choose from:", courses)
        except:
           print("Invalid Course")
    for student in students:
        if student==students:
            print("Same data already exist!")
            return

    student_data={
        "Name":Name,
        "ID":ID,
        "Age":Age,
        "Course":Course
    }
    students.append(student_data)


def store_details():
    with open ("stud_file.txt",'a')as file:
        for i, student in enumerate(students, start=1):
            file.write(
                f"S.No:{i},"
                f"Name: {student['Name']},"
                f"ID: {student['ID']},"
                f"Age: {student['Age']},"
                f"Course: {student['Course']},")

def stud_view():
    if len(students)==0:
        print("No Students found!")
    else:
        print("Student list")
        for student in students:
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            print("_____________")
def search_id():
    search_id=int(input("enter student id"))
    for student in students:
        if ID == search_id:
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            print("_____________")
            return
        else:
            print("ID not found!")

def update_stud():
    update_id=int(input("enter the id to update data:"))
    for student in students:
        if student["ID"] == update_id:
            name=input("Enter a name to update")
            age=int(input("New age:"))
            student["Course"]=course
                  
            if name:
                student["Name"]=name
            if age.isdigit():
                student["Age"]=int(age)
            if course:
                  student["Course"]=course
            print("Student updated successfully!")
            return
        else:
            print("Student not found")

def delete_stud():
    delete_id=int(input("enter student ID to delete:"))
    for student in students:
        if delete_id==ID:
            students.remove(student)
            print("Successfully removed Student details")
            return
        else:
            ("Student not found!")

while True:
    show_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print(" Enter only integer")
        continue


        if choice==1:
            add_stud_details()
            print("Current students list:", students)
        elif choice==2:
            stud_view()
            print("Current students list:", students)
        elif choice==3:
            search_id()
            print("Current students list:", students)
        elif choice==4:
            update_stud()
            print("Current students list:", students)

        elif choice==5:
            delete_stud()
            print("Current students list:", students)
        elif choice==6:
            print("exit")
            break
        else:
            print("Invalid choice")

    
                  
            

    


        
        
    
        

















    


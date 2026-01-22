students=[]
def load_details():
    try:
        with open("stud_file","r") as file:
            for line in file:
                line=line.strip()
                if not line:
                    continue
                parts=line.strip().split(",")
                students={}
                for part in parts:
                    if not part:
                        continue 
                    key,value=part.split(":",1)
                    key,value=key.strip(),value.strip()
                    if key == "Student_id":
                        value = int(value)
                        student["student_id"] = value
                    elif key == "Age":
                        value = int(value)
                        student["Age"] = value
                    elif key == "Name":
                        student["Name"] = value
                    elif key == "Course":
                        student["Course"] = value
                
                if student:
                    students.append(student)
    except FileNotFoundError:
        pass 

def store_details():
    with open ("stud_file.txt",'w')as file:
        for i, student in enumerate(students, start=1):
            file.write(
                f"S.No:{i},"
                f"Name: {student['Name']},"
                f"ID: {student['student_id']},"
                f"Age: {student['Age']},"
                f"Course: {student['Course']},")
    print("All student details saved to 'stud_file.txt'")



def show_menu():
    print("____Student Management System____")
    print("1. Add Student")
    print("2. View All Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def add_stud_details():
    while True:
        try:
            Name = input("Enter student Name: ").strip()
            if Name.isalpha():
                break
            print("Enter only alphabets")
        except ValueError:
            print("Something went wrong with Name input")
            
    while True:
        try:
            student_id=int(input("Enter student ID: "))
            if any(s["ID"]==student_id for s in students):
                print("ID already exist. Enter new")
            else:
                break
        except ValueError:
            print("Enter only Integers")
    while True:
        try: 
            Age= int(input("Enter student Age: "))
            break 
        except ValueError: 
            print("Enter valid number for Age")


    available_courses = ["BCA","BSC","BCOM","BA","MCA"]
    while True:
        course = input(f"Enter student Course {available_courses}: ").upper()
        if course in available_courses:
            break
        print(f" Invalid course! Choose from {available_courses}")
    student_data={
            "Name":Name,
            "student_id":student_id,
            "Age":Age,
            "Course":course
    }
    students.append(student_data)
    return student_data
    




def stud_view():
    if len(students)==0:
        print("No Students found!")
    else:
        print("Student list")
        for student in students:
            print(f"ID: {student['student_id']}")
            print(f"Name: {student['Name']}")
            print(f"Age: {student['Age']}")
            print(f"Course: {student['Course']}")
            print("_____________")


def search_id():
    search_id=int(input("enter student id"))
    for student in students:
        if student["student_id"] ==search_id:
            print(f"ID: {student['student_id']}")
            print(f"Name: {student['Name']}")
            print(f"Age: {student['Age']}")
            print(f"Course: {student['Course']}")
            print("_____________")
            return
        else:
            print("ID not found!")


def update_stud():
    if len(students) ==0:
        print("No students to update!")
        return
    try:
        update_id=int(input("enter the id to update data:"))
        for student in students:
            if student["student_id"] ==update_id:
                name=input("Enter new name")
                age=int(input("Enter New age:"))
                course=input("Enter new course  (BCA/BSC/BCOM/BA/MCA): ")
                if name:
                    student["Name"]=name
                if age:
                    student["Age"]=int(age)
                if course:
                    if course in ["BCA", "BSC", "BCOM", "BA", "MCA"]:
                        student["course"]=course
                else:
                    print("Invalid course, skipping course update.")
            store_details()
            print("Student updated successfully!")
            return
        print("Student noot found!")
    except ValueError:
        print("Invalid input")


def delete_stud():
    try:
        delete_id=int(input("enter student ID to delete:"))
        for student in students:
            if delete_id==student["student_id"]:
                students.remove(student)
                print("Successfully removed Student details")
                return
            else:
                ("Student Details is not added yet!")
    except ValueError:
        print("Invalid ID")
load_details() 
while True:
    show_menu()
    try:
        choice=int(input("Enter your choice: "))

        if choice == 1:
            student=add_stud_details()
            (f" Student '{student['Name']}' added successfully!")
            stud_view()        
            store_details()
        elif choice==2:
            stud_view()
        elif choice==3:
            search_id()
        elif choice ==4:
            update_stud()
        elif choice == 5:
            delete_stud()
        elif choice ==6:
            print(" Exiting program...")
            break
        else:
            print("Invalid choice")

    except ValueError:
        print(" Enter numbers only")
        continue



    
                  
            

    


        
        
    
        

















    

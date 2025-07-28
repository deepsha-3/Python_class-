# class attribute and object instances in python: 

class Student:  # class
  # attributes
    id = ""      
    name = ""
    subject =  ""

# create oject
student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()


# first students details 
student1.id = 1
student1.name = "Dipisha"
student1.subject = "Python"

# second students details 
student2.id = 2
student2.name = "Aashish"
student2.subject = "Java"

# third students details 
student3.id = 3
student3.name = "Kartik"
student3.subject = "C++"

# fourth students details 
student4.id = 4
student4.name = "Karan"
student4.subject = "C"

# print all value
print(f"This is first student details:", {student1.id}, {student1.name}, {student1.subject})
print(f"This is second student details:", {student2.id}, {student2.name}, {student2.subject})
print(f"This is third student details:", {student3.id}, {student3.name}, {student3.subject})
print(f"This is fourth student details:", {student4.id}, {student4.name}, {student4.subject})
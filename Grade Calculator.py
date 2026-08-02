#Student Grade Calculator

#Taking input from user
student_name=input("enter a name:")
Telugu_subject=int(input("enter Telugu subject marks:"))
English_subject=int(input("enter English subject marks:"))
Computers_subject=int(input("enter Computers subject marks:"))
Python_subject=int(input("enter Python subject marks:"))
Java_subject=int(input("enter java subject marks:"))
Total_marks=Telugu_subject+English_subject+Computers_subject+Python_subject+Java_subject
percentage=(Total_marks/500)*100
print("Student Name:", student_name)
print("Total Marks:", Total_marks)
print("Percentage:", round(percentage,2))

#Pass or Fail based on the percentage
if percentage>35:
    print("Pass")
else:
    print("Fail")
    
#Displaying Grades

if percentage>=90:
    print("Grade:A")
elif percentage>=70:
    print("Grade:B")
elif percentage>=60:
    print("Grade:C")
elif percentage>=50:
    print("Grade:D")
else:
    print("Grade:F")
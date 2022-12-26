# WAP to convert marks to grade

grade = str

totalMarks = int(input('Enter your total marks/percentage out of 100 : '))

if(totalMarks>=90 and totalMarks <=100):
    grade = "A+"
    print("Your grade is",grade,".")
elif(totalMarks>=75 and totalMarks <90):
    grade = "A"    
    print("Your grade is",grade,".")
elif(totalMarks>=60 and totalMarks <75):
    grade = "B"
    print("Your grade is",grade,".")
elif(totalMarks>=45 and totalMarks <60):
    grade = "C"
    print("Your grade is",grade,".")
elif(totalMarks>=35 and totalMarks <45):
    grade = "D"
    print("Your grade is",grade,".")
elif(totalMarks>=0 and totalMarks <35):
    grade = "F"
    #You can typecast too.
    print("Your grade is "+ str(grade) +". Better luck next time.")
else:
    print("Invalid input")


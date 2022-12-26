# WAP to find out whether a student is pass or fail
# Criteria : 33% in each subject and 40% of overall

#Assuming total marks per subject is 100.

sub1 = int(input("Enter marks of first subject : "))
sub2 = int(input("Enter marks of second subject : "))
sub3 = int(input("Enter marks of third subject : "))

totalPercent = (sub1 + sub2 + sub3)/3

if (sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("FAIL, BETTER LUCK NEXT TIME.")
    
elif (totalPercent < 40):
    print("FAIL, BETTER LUCK NEXT TIME.")

else:
    print("Congratulations, you PASSED the exam")

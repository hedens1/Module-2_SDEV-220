#Haele Edens - 11/06/2024
#Dean's List or Honor Roll Predictor using GPA
#This app is designed to test if a student qualifies for Dean's List or Honor Roll based on their GPA.

while True:
    #Ask for student's name
    last_name = input("Enter the student's last name (or 'zzz' to quit): ").lower()

    #Exit condition
    if last_name == 'zzz'.lower():
        print("Thank you! Goodbye!")
        break

    #Ask for student's first name 
    first_name = input("Enter the student's first name: ").lower()

    #Ask for student's GPA
    gpa =float(input ("Enter the student's GPA to test if they qualify for Dean's List or Honor Roll: "))

    #Determine if the student qualifies for Dean's List or Honor Roll
    if gpa >= 3.5:
        print(f"{first_name.title()} {last_name.title()} qualifies for the Dean's List!")
    elif gpa >= 3.25:
        print(f"{first_name.title()} {last_name.title()} qualifies for the Honor Roll!")
number1 = input("What is your grade: ")
grade = int(number1)
if grade > 85:
    print("Distinction")
elif 65 <= grade <= 85: 
    print("Pass")
else:
    print("Fail")

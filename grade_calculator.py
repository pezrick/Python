maths_grade = int(input("What is your maths grade: "))
chemistry_grade = int(input("What is your chemistry grade: "))
physics_grade = int(input("What is your physics grade: "))
average_grade = int((maths_grade + chemistry_grade + physics_grade) / 3)

if average_grade >= 70:
    print("A")
elif average_grade >= 60:
    print("B")
elif average_grade >= 50:
    print("C")
elif average_grade >= 40:
    print("D")
else:
    print("You failed!!!")

print(average_grade)
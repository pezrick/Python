def student_grade(name, homework_score, assessment_score, final_exam_score):
    total_percentage = round((homework_score + assessment_score + final_exam_score) / 175 * 100)
    return name, total_percentage

print(student_grade("Pez", 20, 50, 90))
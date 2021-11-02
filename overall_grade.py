def student_grade(name, homework_score, assessment_score, final_exam_score):
    if homework_score > 25:
        return "Invalid Amount Homework"
    elif assessment_score > 50:
        return "Invalid Amount Assessment"
    elif final_exam_score > 100:
        return "Invalid Amount Final Exam"
    else:
        total_percentage = round((homework_score + assessment_score + final_exam_score) / 175 * 100)
        return name, total_percentage

print(student_grade("Pez", 23, 39, 80))
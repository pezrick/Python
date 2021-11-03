class Student:

    def __init__(self, name, age, class_ = "student"):
        self.name = name
        self.age = age
        self.class_ = class_

    def avtestscore(self, score1, score2, score3):
        average = (score1 + score2 + score3)/3
        print(average)

John = Student("John", "21", "non student")

John.avtestscore(20,30,40)


# print(getattr(John, "test2", "test1"))
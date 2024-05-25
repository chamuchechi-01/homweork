class it_academy:
    def __init__(self, student, score, teacher):
        self.student = student
        self.__test_score = score
        self.teacher = teacher

    def get_student(self):
        return self.student

    def get_score(self):
        return self.__test_score

    def get_teacher(self):
        return self.teacher

    def set_student(self, student):
        self.student = student

    def set_test_score(self, score):
        self.__test_score = score

    def set_teacher(self, teacher):
        self.teacher = teacher


it_academy = it_academy("Amir", 85, "Mirafzal")

print(it_academy.get_score())

it_academy.get_student()
print(it_academy.get_student())

it_academy.get_teacher()
print(it_academy.get_teacher())


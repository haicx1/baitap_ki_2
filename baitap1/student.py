import itertools


class Student:
    id_obj = itertools.count()

    def __init__(self):
        self.id = next(Student.id_obj)
        self._name = None
        self._grade = None
        self.next = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if value in range(0, 11):
            self._grade = value
        else:
            raise ValueError('Not grade')

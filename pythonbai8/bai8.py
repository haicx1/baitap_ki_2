class Student:
    def __init__(self):
        self._class_id = []
        self._teacher_id = None
        self._student_id = None
        self._price = None
        self._subject = []
        self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def class_id(self):
        return self._class_id

    @class_id.setter
    def class_id(self, value):
        self._class_id.append(value)

    @property
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        self._teacher_id = value

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject.append(value)

    def display(self):
        print(self._student_id, self._name, *self.subject)


class Manage:
    price_subject = {}
    list_student = []
    teacher = {}

    def search_by_subject(self, input):
        number = 0
        list1 = []
        for student in self.list_student:
            if input in student.subject:
                number = number + 1
                list1.append(student)
        print('So hoc sinh dang hoc:', number)
        for student in list1:
            print(student.name)

    def get_student(self):
        with open('SinhVien', 'r') as fh:
            for x in fh:
                data = x.split()
                student = Student()
                student.student_id = data[0]
                student.name = data[1]
                self.list_student.append(student)
            fh.close()
        with open('Lophoc', 'r') as fh:
            for x in fh:
                ls = []
                data = x.split()
                for student in data[3].split(','):
                    ls.append(student)
                for id in ls:
                    for st in self.list_student:
                        if id == st.student_id:
                            st.subject = data[2]
                            st.class_id = data[0]
            for st in self.list_student:
                st.display()
            fh.close()

    def get_teacher(self, input):
        list_teach = []
        with open('Lophoc', 'r') as fh:
            for x in fh:
                data = x.split()
                if data[1] == input:
                    list_teach.append(data[0])
            fh.close()
        print(input, *list_teach)

    def search_student(self, input):
        for student in self.list_student:
            if input == student.student_id:
                print(student.student_id, student.name, *student.class_id)

    def sort_price(self):
        price = {}

        with open('mon_hoc', 'r') as fh:
            for x in fh:
                data = x.split()
                self.price_subject[data[0]] = int(data[2])
            fh.close()
        for key in self.price_subject.keys():
            price[key] = 0
        for student in self.list_student:
            if data[0] in student.subject:
                price[data[0]] = price[data[0]] + self.price_subject[data[0]]
        sorted_price = sorted(price.items(), reverse=True)
        converted_price = dict(sorted_price)
        print(converted_price)

manage = Manage()
manage.get_student()
manage.search_by_subject('ST0001')
manage.get_teacher('T0001')
manage.search_student('B0001')
manage.sort_price()
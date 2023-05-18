from student import Student


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.name)
            temp = temp.next

    def append(self, student=Student()):
        new_node = student
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, student=Student()):
        new_node = student
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, student=Student()):
        temp = self.get(index)
        if temp:
            temp = student
            return True
        return False

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp


class ManageStudent:
    llist = LinkedList()

    def create_student(self):
        filename = 'student'
        with open(filename, 'w') as fh:
            while True:
                choice = input('Ban co muon nhap SV?(y/n)')
                if choice == 'y':
                    student1 = Student()
                    student1.name = input('Nhap ten:')
                    student1.grade = int(input('nhap diem'))
                    self.llist.append(student1)
                    continue
                elif choice == 'n':
                    break
                else:
                    print('nhap y hoac n')
                    continue
            for i in range(0, self.llist.length):
                student2 = self.llist.get(i)
                fh.write(str(student2.id))
                fh.write('\n')
                fh.write(student2.name)
                fh.write('\n')
                fh.write(str(student2.grade))
                fh.write('\n')
            fh.close()

    def search_student(self):
        search = False
        student_id = int(input('Nhap ma SV:'))
        for i in range(self.llist.length):
            temp = self.llist.get(i)
            if temp.id == student_id:
                temp.display()
                search = True
                return temp
                break
            else:
                return search
        if not search:
            print('Student not found.')

    def update_student(self):
        filename = 'student'
        temp = self.search_student()
        if temp == False:
            return print('Student not found')
        else:
            with open(filename, 'w') as fh:
                choice = int(input('Enter choice(1/2)?'))
                if choice == 1:
                    student = Student()
                    student.name = input('Enter new name:')
                    student.grade = input('Enter new grade:')
                    self.llist.set_value(temp.id, student)
                    for i in range(self.llist.length):
                        student2 = self.llist.get(i)
                        fh.write(str(student2.id))
                        fh.write('\n')
                        fh.write(student2.name)
                        fh.write('\n')
                        fh.write(str(student2.grade))
                        fh.write('\n')
                if choice == 2:
                    self.llist.remove(temp.id)
                    print('Delete Success')


manage = ManageStudent()
manage.update_student()

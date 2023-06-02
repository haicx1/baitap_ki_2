class User:
    def __init__(self):
        self._name = None
        self._ticket = None
        self.next = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def ticket(self):
        return self._ticket

    @ticket.setter
    def ticket(self, value):
        self._ticket = value

    def display(self):
        print('Name:', self.name)
        print('Ticket:', self.ticket)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            temp.display()
            temp = temp.next

    def append(self, user=User()):
        new_node = user
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


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            temp.display()
            temp = temp.next

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


class ManageTicket:
    llist = LinkedList()

    def insert_buyer(self, n):
        for i in range(n):
            user = User()
            user.name = input('Enter name:')
            user.ticket = int(input('Enter number of ticket want to buy:'))
            self.llist.append(user)

    def buy_ticket(self, amount1):
        temp = self.llist.get(0)
        if temp.ticket > amount1:
            return False
        else:
            new_amount = amount1 - temp.ticket
            self.llist.pop_first()
            return new_amount


n1 = int(input('Nhap so nguoi muon mua ve:'))
amount = int(input('Nhap so ve co:'))
manage = ManageTicket()
manage.insert_buyer(n1)
while True:
    temp = manage.buy_ticket(amount)
    if temp == False:
        print('Het ve')
        break
manage.llist.print_list()

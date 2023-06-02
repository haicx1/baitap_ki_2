class Customer:
    def __init__(self):
        self._id = None
        self._name = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Goods:
    def __init__(self):
        self._id = None
        self._name = None
        self._price = None
        self._quantity = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value


class Bill:
    def __init__(self):
        self._customer_id = None
        self._customer_name = None
        self._id = None
        self._name = None
        self._price = None
        self._quantity = None
        self._total = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def display(self):
        print(self.customer_id, self.customer_name, self._id, self._name, self._price, self._quantity, self._total)


class Manage:
    list1 = []
    list2 = []

    def get_data(self):
        with open('customers.txt', 'r') as fh:
            with open('products.txt', 'r') as fh1:
                for x in fh:
                    data = x.split()
                    customer = Customer()
                    customer.id = data[0]
                    customer.name = data[1]
                    self.list1.append(customer)
                for y in fh1:
                    data = y.split()
                    product = Goods()
                    product.id = data[0]
                    product.name = data[1]
                    product.price = data[2]
                    self.list2.append(product)
                fh1.close()
            fh.close()

    def create_bill(self, quantity, input1, input2):
        with open('bills.txt', 'a') as fh:
            for customer in self.list1:
                if input1 == customer.id:
                    fh.write(customer.id)
                    fh.write('    ')
                    fh.write(customer.name)
                    fh.write('    ')
                    break
            for product in self.list2:
                if input2 == product.id:
                    product.quantity = quantity
                    fh.write(product.id)
                    fh.write('    ')
                    fh.write(product.name)
                    fh.write('    ')
                    fh.write(product.price)
                    fh.write('    ')
                    fh.write(product.quantity)
                    fh.write('\n')
                    break

    def search_bill(self, input):
        with open('bills.txt', 'r') as fh:
            for x in fh:
                data = x.split()
                if input == data[0]:
                    print(*data)

    def sort_bill(self):
        list = []
        with open('bills.txt', 'r') as fh:
            for x in fh:
                data = x.split()
                bill = Bill()
                bill.customer_id = data[0]
                bill.customer_name = data[1]
                bill.id = data[2]
                bill.name = data[3]
                bill.price = data[4]
                bill.quantity = data[5]
                bill.total = int(bill.price) * int(bill.quantity)
                list.append(bill)
            fh.close()
        list.sort(key=lambda y: y.total)
        for bill in list:
            bill.display()


manage = Manage()
manage.get_data()
n = int(input())
for i in range(n):
    input1 = input('Nhap ma KH:')
    input2 = input('Nhap ma H:')
    quantity = input('Nhap So luong:')
    manage.create_bill(quantity, input1, input2)
input3 = input()
manage.search_bill(input3)
manage.sort_bill()

class Product:
    def __init__(self, name, price, description, size_category):
        self.name = name
        self.price = price
        self.description = description
        self.size_category = size_category

    def show_info(self):
        print(f"Назва: {self.name}")
        print(f"Ціна: {self.price} грн")
        print(f"Опис: {self.description}")
        print(f"Розмір: {self.size_category.capitalize()}")
        print("〜" * 30)


class Customer:
    def __init__(self, first_name, last_name, number, address=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.address = address
        self.email = email

    def show_info(self):
        print(f"Customer: {self.first_name} {self.last_name}")
        print(f"Number: {self.number}")
        if self.address:
            print(f"Addres: {self.address}")
        if self.email:
            print(f"Email: {self.email}")
        print("〜" * 30)


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = {}

    def add_product(self, product, quantity=1):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def total_price(self):
        return sum(product.price * qty for product, qty in self.items.items())

    def __str__(self):
        result = [
            f"Customer: {self.customer.first_name} {self.customer.last_name}",
            "〜" * 30,
            "Замовлення для " + self.customer.first_name + " " + self.customer.last_name,
            "Товари:"
        ]

        for product, qty in self.items.items():
            total = product.price * qty
            result.append(f"\n- {product.name} ({qty} шт.) по {product.price} грн = {total} грн")

        result.append("〜" * 30)
        result.append(f"Загальна сума: {self.total_price()} грн")
        return '\n'.join(result)


product1 = Product(
    name="Пилосос5000",
    price=3499,
    description="Потужний пилосос без мішка для збору пилу.",
    size_category="великий"
)

product2 = Product(
    name="НавушникиProMaxUltra",
    price=799,
    description="Бездротові навушники з шумозаглушенням.",
    size_category="маленький"
)

# product1.show_info()
# product2.show_info()

customer1 = Customer(
    first_name="Levi",
    last_name="Ackerman",
    number="+380",
    address="Paradis Island",
    email="<EMAIL>"
)

# customer1.show_info()

order1 = Order(customer1)
order1.add_product(product1, quantity=1)
order1.add_product(product2, quantity=1)


assert isinstance(order1.customer, Customer), "Екземпляр класу Customer"
assert order1.total_price() == 4298, "Сума має бути 4298 грн"

order1.add_product(product1, quantity=2)
assert order1.total_price() == 4298 + 2 * 3499, "Сума має враховувати 2 нових товару"


print(order1)







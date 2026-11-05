class Product:
    """Товар интернет-магазина."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict, products: list["Product"] | None = None) -> "Product":
        if products:
            for product in products:
                if product.name == product_data["name"]:
                    product.quantity += product_data["quantity"]
                    product.price = max(product.price, product_data["price"])
                    return product
        return cls(**product_data)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            answer = input("Цена понижается. Подтвердить? (y/n): ")
            if answer == "y":
                self.__price = new_price
        else:
            self.__price = new_price

    def __str__(self) -> str:
        price = self.price
        if float(price).is_integer():
            price = int(price)
        return f"{self.name}, {price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        return self.price * self.quantity + other.price * other.quantity


class Category:
    """Категория товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            result += f"{product}\n"
        return result

    @property
    def get_products_list(self) -> list[Product]:
        return self.__products

    def __str__(self) -> str:
        total = 0
        for product in self.__products:
            total += product.quantity
        return f"{self.name}, количество продуктов: {total} шт."


class CategoryIterator:
    """Перебор товаров категории."""

    def __init__(self, category: Category):
        self.category = category
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self) -> Product:
        if self.index < len(self.category.get_products_list):
            product = self.category.get_products_list[self.index]
            self.index += 1
            return product
        raise StopIteration

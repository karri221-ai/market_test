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
            price = product.price
            if float(price).is_integer():
                price = int(price)
            result += f"{product.name}, {price} руб. Остаток: {product.quantity} шт.\n"
        return result

import pytest
from src.classes import BaseProduct, Category, CategoryIterator, LawnGrass, Product, Smartphone


@pytest.fixture
def product():
    return Product("Samsung Galaxy", "256GB, серый", 180000.0, 5)


def test_product_init(product):
    assert product.name == "Samsung Galaxy"
    assert product.description == "256GB, серый"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_init(product):
    category = Category("Смартфоны", "Мобильные телефоны", [product])

    assert category.name == "Смартфоны"
    assert category.description == "Мобильные телефоны"
    assert "Samsung Galaxy" in category.products


def test_category_count(product):
    Category("Смартфоны", "Описание", [product])
    Category("Телевизоры", "Описание", [product])

    assert Category.category_count == 2


def test_product_count(product):
    Category("Смартфоны", "Описание", [product, product, product])

    assert Category.product_count == 3


def test_add_product(product):
    category = Category("Смартфоны", "Описание", [])
    category.add_product(product)

    assert Category.product_count == 1
    assert "Samsung Galaxy" in category.products


def test_products_getter(product):
    category = Category("Смартфоны", "Описание", [product])

    assert category.products == "Samsung Galaxy, 180000 руб. Остаток: 5 шт.\n"


def test_new_product():
    product = Product.new_product(
        {"name": "Тест", "description": "Описание", "price": 500.0, "quantity": 2}
    )

    assert product.name == "Тест"
    assert product.price == 500.0


def test_price_setter_valid(product):
    product.price = 200000.0

    assert product.price == 200000.0


def test_price_decrease_confirmed(product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 100.0

    assert product.price == 100.0


def test_price_decrease_cancelled(product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 100.0

    assert product.price == 180000.0


def test_price_setter_invalid(product, capsys):
    product.price = -10

    assert product.price == 180000.0
    assert "Цена не должна быть нулевая или отрицательная" in capsys.readouterr().out


def test_new_product_duplicate_higher_price(product):
    result = Product.new_product(
        {"name": "Samsung Galaxy", "description": "Описание", "price": 190000.0, "quantity": 3},
        [product],
    )

    assert result is product
    assert product.quantity == 8
    assert product.price == 190000.0


def test_new_product_duplicate_lower_price(product):
    Product.new_product(
        {"name": "Samsung Galaxy", "description": "Описание", "price": 150000.0, "quantity": 2},
        [product],
    )

    assert product.quantity == 7
    assert product.price == 180000.0


def test_new_product_not_duplicate(product):
    result = Product.new_product(
        {"name": "Другой товар", "description": "Описание", "price": 500.0, "quantity": 1},
        [product],
    )

    assert result is not product
    assert result.name == "Другой товар"
    assert product.quantity == 5


def test_product_str(product):
    assert str(product) == "Samsung Galaxy, 180000 руб. Остаток: 5 шт."


def test_category_str(product):
    other = Product("Iphone 15", "512GB", 210000.0, 8)
    category = Category("Смартфоны", "Описание", [product, other])

    assert str(category) == "Смартфоны, количество продуктов: 13 шт."


def test_product_add(product):
    other = Product("Iphone 15", "512GB", 210000.0, 8)

    assert product + other == 2580000.0


def test_category_iterator(product):
    other = Product("Iphone 15", "512GB", 210000.0, 8)
    category = Category("Смартфоны", "Описание", [product, other])

    result = list(CategoryIterator(category))

    assert result == [product, other]


def test_category_iterator_twice(product):
    category = Category("Смартфоны", "Описание", [product])
    iterator = CategoryIterator(category)

    assert len(list(iterator)) == 1
    assert len(list(iterator)) == 1


def test_category_iterator_empty():
    category = Category("Пусто", "Описание", [])

    assert list(CategoryIterator(category)) == []


def test_smartphone_init():
    phone = Smartphone("Samsung", "256GB", 180000.0, 5, 95.5, "S23", 256, "Серый")

    assert phone.name == "Samsung"
    assert phone.efficiency == 95.5
    assert phone.model == "S23"
    assert phone.memory == 256
    assert phone.color == "Серый"


def test_lawn_grass_init():
    grass = LawnGrass("Трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый")

    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_add_same_class():
    grass1 = LawnGrass("Трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Трава 2", "Описание", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    assert grass1 + grass2 == 16750.0


def test_add_different_classes():
    phone = Smartphone("Samsung", "256GB", 180000.0, 5, 95.5, "S23", 256, "Серый")
    grass = LawnGrass("Трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError):
        phone + grass


def test_add_product_invalid():
    category = Category("Тест", "Описание", [])

    with pytest.raises(TypeError):
        category.add_product("Not a product")

    assert Category.product_count == 0


def test_add_product_subclass():
    category = Category("Смартфоны", "Описание", [])
    phone = Smartphone("Samsung", "256GB", 180000.0, 5, 95.5, "S23", 256, "Серый")
    category.add_product(phone)

    assert Category.product_count == 1


def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        BaseProduct()


def test_mixin_prints_product(capsys):
    Product("Продукт1", "Описание продукта", 1200, 10)

    assert capsys.readouterr().out == "Product('Продукт1', 'Описание продукта', 1200, 10)\n"


def test_mixin_prints_subclass_name(capsys):
    Smartphone("Samsung", "256GB", 180000.0, 5, 95.5, "S23", 256, "Серый")

    assert capsys.readouterr().out == "Smartphone('Samsung', '256GB', 180000.0, 5)\n"

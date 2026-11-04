import pytest
from src.classes import Category, Product


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
    product.price = 100.0

    assert product.price == 100.0


def test_price_setter_invalid(product, capsys):
    product.price = -10

    assert product.price == 180000.0
    assert "Цена не должна быть нулевая или отрицательная" in capsys.readouterr().out

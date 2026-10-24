import pytest
from src.classes import Category, Product


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


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
    assert isinstance(category.products[0], Product)


def test_category_count(product):
    Category("Смартфоны", "Описание", [product])
    Category("Телевизоры", "Описание", [product])

    assert Category.category_count == 2


def test_product_count(product):
    Category("Смартфоны", "Описание", [product, product, product])

    assert Category.product_count == 3

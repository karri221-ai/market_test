from src.classes import Category
from src.utils import load_categories


def test_load_categories():
    categories = load_categories("data/products.json")

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert "Iphone 15" in categories[0].products
    assert Category.product_count == 4

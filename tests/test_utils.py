from src.classes import Category
from src.utils import load_categories


def test_load_categories():
    categories = load_categories("data/products.json")

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 3
    assert isinstance(categories[0], Category)

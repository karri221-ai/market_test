import json

from src.classes import Category, Product


def load_categories(path: str) -> list[Category]:
    """Читает JSON-файл и возвращает список объектов Category."""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for item in data:
        products = [Product(**product_data) for product_data in item["products"]]
        category = Category(item["name"], item["description"], products)
        categories.append(category)

    return categories

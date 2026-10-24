# Market Test
Ядро интернет-магазина. 

## Реализовано
   - Класс Product: название, описание, цена, количество
   - Класс Category: название, описание, список товаров
   - Автоматические счётчики категорий и товаров
   - Тесты на pytest, покрытие 100%
   - Загрузка категорий и товаров из JSON-файла (`load_categories`)

## Установка и запуск
poetry install
poetry run python main.py
poetry run pytest --cov=src

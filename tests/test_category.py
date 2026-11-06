def test_category(category1, category2):
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products.split("\n")) == 4 # в конце последний строки есть перенос, результат кол-во продуктов +1
    assert category1.category_count == 2
    assert category1.product_count == 4

    assert category2.name == "Телевизоры"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category2.products.split("\n")) == 2 # в конце последний строки есть перенос, результат кол-во продуктов +1
    assert category2.category_count == 2
    assert category2.product_count == 4



def test_category_add_product(category2, product):
    category2.add_product(product)
    assert len(category2.products.split("\n")) == 3 # в конце последний строки есть перенос, результат кол-во продуктов +1
    assert category2.category_count == 3
    assert category2.product_count == 5

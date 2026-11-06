def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_dict(product_dict):
    assert product_dict.name == "Iphone 15"
    assert product_dict.description == "512GB, Gray space"
    assert product_dict.price == 210000.0
    assert product_dict.quantity == 8


def test_product_setter(capsys, product):
    product.price = 800
    assert product.price == 800
    product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 800
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 800
    product.price = 500
    assert product.price == 500
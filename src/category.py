class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавляет новый продукт в список"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает список продуктов"""
        list_products = ""
        for product in self.__products:
            list_products += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return list_products




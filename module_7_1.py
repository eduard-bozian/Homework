class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"
class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read()
    def add(self, *products):
        existing_products = set()
        with open(self.__file_name, 'r') as file:
            for line in file:
                existing_products.add(line.split(',')[0].strip())
        for product in products:
            if product.name in existing_products:
                print(f"Продукт {product.name} уже есть в магазине")
                file.close()
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')
                existing_products.add(product.name)


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print(str(p2))
    s1.add(p1, p2, p3)
    print(s1.get_products())

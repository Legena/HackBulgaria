class Product():
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, ram):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.ram = ram


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price,
        display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store():
    products = {}
    profit = 0

    def __init__(self, name):
        self.name = name

    def load_new_products(self, product, count):
        if(product in self.products):
            self.products[product] += count
        else:
            self.products[product] = count

    def list_products(self, Product):
        for product in self.products:
            if isinstance(product, Product):
                print(product.name, self.products[product])

    def sell_product(self, product):
        if(product in self.products):
            if(self.products[product] > 0):
                self.products[product] -= 1
                self.profit += product.profit()
                return True
        return False

    def total_income(self):
        return self.profit


def main():
    store = Store('Laptop.bg')
    smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
    store.load_new_products(smarthphone, 2)
    store.list_products(Smartphone)
    print(store.sell_product(smarthphone))
    print(store.sell_product(smarthphone))

    print(store.total_income())


if __name__ == "__main__":
    main()
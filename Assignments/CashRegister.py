class CashRegister:

    TAX_RATE = 0.05

    def __init__(self, cashier_name):
        self.cashier_name = cashier_name
        self.products = []


    def add_product_in_purchase(self, product, quantity=1):
        product_to_find = self.get_product_dict_by_name(product["name"])

        if isinstance(product, dict) and "name" in product and "price" in product and isinstance(product["price"], (int, float)) and product_to_find is None:
            product["quantity"] = quantity
            self.products.append(product)
        else:
            print("Please add a valid product")

        return self


    def set_item_quantity(self, product_name, quantity):
        product = self.get_product_dict_by_name(product_name)

        if product is not None:
            product["quantity"] = quantity
        else:
            print("Please add a valid product")

    def display_products_in_purchase(self):
        if len(self.products) != 0:
            print(self.get_product_names())
    

    def remove_product(self, product_name):
        product = self.get_product_dict_by_name(product_name)

        if product is not None:
            self.products.remove(product)
        else:
            print("Please enter a valid product")
    

    def update_product_price(self, product_name, new_price):
        product = self.get_product_dict_by_name(product_name)

        if product is not None and isinstance(new_price, (int, float)):
            product["price"] = new_price
        else:
            print("Please enter a valid product")


    def calculate_subtotal(self):
        subtotal = 0

        if len(self.products) == 0:
            return subtotal

        for product in self.products:
            subtotal += product["price"] * product["quantity"]

        return subtotal


    def calculate_taxes(self):
        return self.calculate_subtotal() * CashRegister.TAX_RATE

    

    def calculate_total_with_taxes(self):
        return self.calculate_subtotal() + self.calculate_taxes()
    

    def clear_purchase(self):
        return self.products.clear()
    

    def get_product_names(self):
        product_list = []
        for product in self.products:
            product_list.append(product["name"])
        
        return product_list
    

    def get_product_dict_by_name(self, product_name):
        for product in self.products:
            if product_name == product["name"]:
                return product
        
        return None
        
# Instantiate object and call methods
a = CashRegister("Tin")

donut = {"name": "Donut", "price": 20}
donut2 = {"name": "Donut", "price": 20}
coffee = {"name": "Coffee", "price": 80}
garlic_bread = {"name": "Garlic Bread", "price": 120}
a.add_product_in_purchase(donut).add_product_in_purchase(coffee).add_product_in_purchase(donut2)

a.display_products_in_purchase()

a.set_item_quantity("Donut", 5)
print(f"Before price update: {a.products}")

a.update_product_price("Donut",60)
print(f"After price update: {a.products}")

print(f"Subtotal: {a.calculate_subtotal()}")
print(f"Taxes: {a.calculate_taxes()}")
print(f"Total: {a.calculate_total_with_taxes()}")

print(a.cashier_name)
a.clear_purchase()
print(a.products)
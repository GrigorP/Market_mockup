class Product:
    def __init__(self, name: str, price: float, quantity: int, prod_id: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.prod_id = prod_id
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.prod_id == other.prod_id
        return False

    def show_info(self):
        return f"Name: {self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}, Product ID: {self.prod_id}"

    def decrement_quantity(self):
        if self.quantity > 0:
            self.quantity -= 1
        else:
            raise ValueError("Product quantity cannot be negative")


class Magazine:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        if product not in self.products:
            self.products.append(product)
            return "Product added successfully."
        return "Product already exists."

    def show_products(self):
        if not self.products:
            return "No products found."
        return '\n'.join([product.show_info() for product in self.products])

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)
            return "Product removed successfully."
        return "Product not found."


class Buyer:
    def __init__(self, name: str, balance: float, buyer_id: int):
        self.name = name
        self.balance = balance
        self.buyer_id = buyer_id
        self.purchased_products = []
        self.cart = []

    def show_balance(self):
        return f"{self.balance:.2f}"

    def show_purchased_products(self):
        if not self.purchased_products:
            return "No products purchased."
        return '\n'.join([product.show_info() for product in self.purchased_products])

    def show_cart(self):
        if not self.cart:
            return "Cart is empty."
        return '\n'.join([product.show_info() for product in self.cart])

    def buy_product(self, magazine: Magazine, product: Product):
        if product in magazine.products and product.quantity > 0:
            if product.price <= self.balance:
                product.decrement_quantity()
                self.purchased_products.append(product)
                self.balance -= product.price
                return f"Product purchased: {product.show_info()}"
            return "Insufficient funds."
        return "Product out of stock or not found in magazine."

    def add_to_cart(self, product: Product):
        if product not in self.cart:
            self.cart.append(product)
            return "Product added to cart successfully."
        return "Product already in cart."

    def buy_from_cart(self, magazine: Magazine, product: Product):
        if product in self.cart:
            result = self.buy_product(magazine, product)
            if "purchased" in result.lower():
                self.cart.remove(product)
            return result
        return "Product not found in cart."


def main():
    product1 = Product("Men's Straight-Fit Stretch Bootcut Jean", 30.40, 5, 1111)
    product2 = Product("Lee Men's Extreme Motion Straight Taper Jean", 33.11, 5, 2222)
    product3 = Product("Men's Slim-Fit Stretch Jean", 23.90, 5, 3333)

    magazine = Magazine()
    print(magazine.add_product(product1))
    print(magazine.add_product(product2))
    print(magazine.add_product(product3))

    buyer = Buyer("Grigor", 100.00, 1234)
    print(buyer.add_to_cart(product1))
    print(buyer.buy_from_cart(magazine, product1))


if __name__ == "__main__":
    main()
# main.py
from pages import HomePage, LoginPage
from utils import add_numbers, reverse_string, is_even
from models import User, Product

if __name__ == "__main__":
    # Pages
    home = HomePage()
    print(home.welcome())

    login = LoginPage()
    print(login.login("admin", "1234"))
    print(login.login("user", "wrong"))

    # Utils
    print("Sum:", add_numbers(5, 10))
    print("Reverse:", reverse_string("hello"))
    print("Is 8 even?", is_even(8))

    # Models
    user = User("rokibul", "rokibul@example.com")
    print(user.get_info())

    product = Product("Laptop", 75000)
    print(product.details())

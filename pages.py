# pages.py
# Dummy example of Python Page classes (for learning only)

class BasePage:
    def __init__(self, title):
        self.title = title

    def show_title(self):
        return f"Page Title: {self.title}"


class HomePage(BasePage):
    def __init__(self):
        super().__init__("Home Page")

    def welcome_message(self):
        return "Welcome to the Home Page!"


class LoginPage(BasePage):
    def __init__(self):
        super().__init__("Login Page")

    def login(self, username, password):
        # Dummy login function
        if username == "admin" and password == "1234":
            return "Login successful!"
        else:
            return "Login failed."


# Example usage
if __name__ == "__main__":
    home = HomePage()
    print(home.show_title())
    print(home.welcome_message())

    login = LoginPage()
    print(login.show_title())
    print(login.login("admin", "1234"))
    print(login.login("user", "wrongpass"))

from selenium.webdriver.common.by import By



class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_input = (By.ID,"username")
        self.password_input = (By.ID,"password")
        self.login_button = (By.CLASS_NAME,"radius")
        self.flash_message = (By. ID,"flash")

    def load(self):
        """Otwiera stronę logowania."""
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        """Wprowadza dane logowania i klika przycisk logowania."""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_message(self):
        """Zwraca wiadomość po próbie logowania."""
        return self.driver.find_element(*self.flash_message).text

    def getTittle(self):
        return self.driver.title


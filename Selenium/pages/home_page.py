from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
    
class HomePage:
    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)

    def go_to(self):
        self.selenium_driver.get("https://www.saucedemo.com/")
        self.selenium_driver.maximize_window()

    def login(self, username, password):
        username_locator = (By.ID, "user-name")
        wait_username = self.wait.until(EC.element_to_be_clickable(username_locator))
        wait_username.click()
        wait_username.clear()
        wait_username.send_keys(username)
        password_field = self.selenium_driver.find_element(By.id, "password")
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

    def login_button(self):
        login_button = self.selenium_driver.find_element(By.ID, "login-button")
        login_button.click()
    
    def products_verif(self):
        products_verif_locator= (By.XPATH, "//span[@class='title' and text()='Products']")
        wait_products_verif_= self.wait.until(EC.presence_of_element_located(products_verif_locator))
        products_verif_locator = wait_products_verif_.text
        assert products_verif_locator == "Products"
        
    def add_to_cart(self):
        product1 = self.selenium_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        product1.click()

    def add_to_cart2(self):
        product2= self.selenium_driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        product2.click()

    def click_on_cart(self):
        click_on_cart=self.selenium_driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        click_on_cart.click() 

    def your_cart_verif(self):
        your_cart_locator= (By.XPATH, "//span[@class='title' and text()='Your Cart']")
        wait_cart= self.wait.until(EC.presence_of_element_located(your_cart_locator))
        your_cart_locator=wait_cart.text 
        assert your_cart_locator == "Your Cart"

    def products_in_the_cart_verif(self):
        product1= self.selenium_driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div[@class='inventory_item_name']")
        product2= self.selenium+driver.find.element(By.XPATH, "//a[@id='item_0_title_link']/div[@class='inventory_item_name']")
        assert product1.text == "Sauce Labs Backpack"
        assert product2.text == "Sauce Labs Bike Light" 

    def checkout_(self):
        checkout_=self.selenium_driver.find_element(By.ID, "checkout")
        checkout_.click()
        


    def your_info_verif(self):
        your_info=(By.XPATH, "//span[@class='title' and contains(text(),'Checkout: Your Information')]")
        wait_your_info=self.wait.until(EC.presence_of_element_located(your_info))
        your_info_text=wait_your_info.text
        assert your_info_text == "Checkout: Your Information"ChildProcessError


    def fill_checkout_fields(self, name, last_name, postal_code):
        name_locator=(By.ID, "first-name")
        wait_name=self.wait.until(EC.element_to_be_clickable(name_locator))
        wait_name.click()
        wait_name.clear()
        
        last_name_locator = (By.ID, "last-name")
        wait_last_name = self.wait.until(EC.element_to_be_clickable(last_name_locator))
        wait_last_name.click()
        wait_last_name.clear()
        wait_last_name.send_keys(last_name)

        postal_code= (By.ID, "postal-code")
        wait_postal_code = self.wait.until(EC.element_to_be_clickable(postal_code))
        wait_postal_code.click()
        wait_postal_code.clear()
        wait_postal_code.send_keys(zip_code)

        continue_button=self.selenium_driver.find_element(By.ID, "continue")
        continue_button.click()

    def checkout_overview_verif(self):
        checkout_overview_locator=(By.XPATH, "//span[@class='title']")
        wait_checkout_overview_field = self.wait.until(EC.presence_of_element_located(checkout_overview_locator))
        checkout_overview_locator= wait_checkout_overview_field.text
        assert checkout_overview_locator == "Checkout: Overview"
        

    def product1_verif(self):
        product1=self.selenium_driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div[@class='inventory_item_name']")
        assert product1.text == "Sauce Labs Backpack"

    def product2_verif(self)
        product2= self.selenium_driver.find_element(By.XPATH, "//a[@id='item_0_title_link']/div[@class='inventory_item_name']")
        assert product2.text == "Sause Labs Bike Light"
    
    def finish(self):
        finish_locator= self.selenium_driver.find_element(By.ID, "finish")
        finish_locator.click()
    
    def checkout_complete(self):
        checkout_complete_locator = (By.XPATH, "//span[@class='title' and text()='Checkout: Complete!']")
        wait_checkout_complete = self.wait.until(EC.presence_of_element_located(checkout_complete_locator))
        checkout_complete_text = wait_checkout_complete.text
        expected_title = "Checkout: Complete!"
        assert checkout_complete_text == expected_title


    def click_on_menu(self):
        menu_locator= (By.ID, "react-burger-menu-btn")
        wait_menu_locator=self.wait.until(EC.element_to_be_clickable(menu_locator))
        wait_menu_locator.click()

    def logout(self):
        logout_locator=(By.ID, "logout_sidebar_link")
        wait_logout_locator=self.wait.until(EC.element_to_be_clickable(logout_locator))
        wait_logout_locator.click()

    
    def login_verif():
        expected_title = "Swag Labs"
        title = self.selenium_driver.title
        assert title == expected_title


        




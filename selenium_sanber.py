import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("standard_user") # isi Username
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,('button[type=submit]')).submit() # klik Login

        # validasi
        # self.assertEqual(response_message, 'Menampilkan halaman produk')

    def test_b_failed_login_with_empty_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("standard_user") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,('button[type=submit]')).submit() # klik Login

        # validasi
        # self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Epic sadface: Password is required')

    def test_c_failed_login_with_empty_email_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"email").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,('button[type=submit]')).submit() # klik tombol masuk

        # validasi
        # self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Epic sadface: Username is required')
        
    def test_d_failed_login_with_empty_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,('button[type=submit]')).submit() # klik Login

        # validasi
        # self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Epic sadface: Username is required')
        
    def test_e_failed_login_with_email_and_password_invalid(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"email").send_keys("standard_user") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("xaver") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,('button[type=submit]')).submit() # klik Login

        # validasi
        # self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
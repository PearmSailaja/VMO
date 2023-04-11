import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Login():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    def TC_001_Blank_Login(self):
        self.login=self.driver.find_element(By.ID,'js-login-btn')
        self.login.click()
        time.sleep(5)
    def TC_002_InvalidEmailId(self,email,pwd):
        self.email=email
        self.pwd=pwd
        self.email_path=self.driver.find_element(By.ID,"login-username")
        self.email_path.send_keys(self.email)
        self.pwd_path = self.driver.find_element(By.ID,"login-password")
        self.pwd_path.send_keys(self.pwd)
        self.login.click()
        time.sleep(5)
    def TC_003_OnlyEmail_Login(self,Email):
        self.email_path.clear()
        self.email_path1 = self.driver.find_element(By.ID, "login-username")
        self.email_path.send_keys(Email)
        self.login.click()
        time.sleep(5)
    def TC_004_Valid_Login(self,Email,Pswd):
        self.email_path.clear()
        self.pwd_path.clear()
        # self.email_path1 = self.driver.find_element(By.ID, "login-username")
        self.email_path.send_keys(Email)
        self.pwd_path.send_keys(Pswd)
        self.login.click()
        time.sleep(5)
        self.driver.quit()



obj=Login()
obj.TC_001_Blank_Login()
obj.TC_002_InvalidEmailId("sailusailu10152gmail.com","Saima@123")
obj.TC_003_OnlyEmail_Login("sailusailu1015@gmail.com")
obj.TC_004_Valid_Login("sailusailu1015@gmail.com","Saima@123")

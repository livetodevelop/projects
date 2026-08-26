from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# this is for my school portal thing
# change these to whatever u need

USERNAME = "your_username_here"
PASSWORD = "your_password_here"  # lol storing passwords in plain text but idc

def setup_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # uncomment if u dont wanna see the browser
    return webdriver.Chrome(options=options)

def login(driver, url):
    driver.get(url)
    
    try:
        # wait for elements to load
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = driver.find_element(By.ID, "password")
        submit_btn = driver.find_element(By.ID, "submit")
        
        # fill in credentials
        username_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)
        submit_btn.click()
        
        print("logged in!")
        time.sleep(2)
        
    except Exception as e:
        print(f"login failed: {e}")

def fill_form(driver, answers):
    """fill out form with given answers"""
    for field_id, value in answers.items():
        try:
            field = driver.find_element(By.ID, field_id)
            field.clear()
            field.send_keys(value)
            print(f"filled {field_id}")
        except:
            print(f"couldnt find field {field_id}")

if __name__ == "__main__":
    driver = setup_driver()
    
    # example usage - change url and answers for your needs
    login_url = "https://example-school-portal.com/login"
    login(driver, login_url)
    
    # sample form data
    form_answers = {
        "question_1": "The answer is 42",
        "question_2": "I agree to the terms",
        "comments": "this is automated lol"
    }
    
    # fill_form(driver, form_answers)
    
    # keep browser open
    input("press enter to close...")
    driver.quit()

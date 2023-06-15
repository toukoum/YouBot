from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

SERVICE_PATH = "/home/toukoum/Documents/chromedriver_linux64/chromedriver.exe"
Service = Service(SERVICE_PATH)
driver = webdriver.Chrome(service=Service)


driver.get("https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?response_type=code&client_id=410783931365-r1iqaudsf3dqpe0g911e1pb2ttile602.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2F&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fyoutube.upload&state=LxPZYksBpDGzFDHdfwa06Bct5rxVer&access_type=offline&service=lso&o2v=1&flowName=GeneralOAuthFlow")
print(driver.title)


search = driver.find_element(By.NAME, "identifier")
search.send_keys("toukoumcode@gmail.com")
search.send_keys(Keys.RETURN)
#search.send_keys("test")
#search.send_keys(Keys.RETURN)
    

time.sleep(30)
driver.quit()
import json
import os
import jwt
from datetime import datetime
from time import sleep
import requests
import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

tfile = "backend\\script\\file\\token.txt"

def modeus_login(email, password):
    driver = selenium.webdriver.Chrome()
    url = "https://utmn.modeus.org/"
    driver.get(url)
    
    #UTMNа
    UTMN_USERFIELD = (By.ID, "userNameInput")
    UTMN_PASSWORDFIELD = (By.ID, "passwordInput")
    UTMN_SUBMIT_BUTTON = (By.ID, "submitButton")
    
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(UTMN_USERFIELD)).send_keys(email)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(UTMN_PASSWORDFIELD)).send_keys(password)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(UTMN_SUBMIT_BUTTON)).click()
    
    sess_js = None
    i = 1
    while (not sess_js):
        sleep(1)
        i += 1
        print("Getting session token " + str(i))
        storage = driver.execute_script("return window.sessionStorage")
        sess_js = [v for k, v in storage.items() if "oidc.user:http" in k]
    
    session = json.loads(sess_js[0])
    token = session['id_token']
    f = open(tfile, "w")
    f.write(token)
    f.close()
    return token

def loginMOD(email, password):
    if (os.path.exists(tfile)):
        token = open(tfile, "r").read()
        decoded = jwt.decode(token, options={"verify_signature": False})
        if (datetime.utcfromtimestamp(decoded['exp']) < datetime.utcnow()):
            token = modeus_login(email, password)
    else:
        token = modeus_login(email, password)

    print(token)
    return token

email = "stud0000193420@study.utmn.ru"
password='Ven13Kodo25$20@#'
loginMOD(email, password)
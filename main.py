from selenium import webdriver
import time

from dotenv import *

options = webdriver.ChromeOptions()
options.binary_location = BRAVE_PATH

navegador = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

email = str(input("Digite o seu email para fazer login no YouTube: "))
senha = str(input("Digite a senha para o respectivo email: "))

navegador.get("https://accounts.google.com/signin/v2/identifier?service=youtube")

navegador\
    .find_element_by_xpath('//*[@id="identifierId"]')\
    .send_keys("{}".format(email))

time.sleep(1)

navegador\
    .find_element_by_xpath('//*[@id="identifierNext"]/div/button')\
    .click()

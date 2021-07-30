from selenium import webdriver
import time

from keys import var


def main():
    def getEmail():
        email = str(input("Digite o seu email para fazer login no YouTube: "))
        return email

    def getPassword():
        senha = str(input("Digite a senha para o respectivo email: "))
        return senha

    options = webdriver.ChromeOptions()
    options.binary_location = var.BRAVE_PATH

    navegador = webdriver.Chrome(
        executable_path=var.DRIVER_PATH, options=options)

    # email = getEmail()
    # senha = getPassword()

    email = var.EMAIL_ADDRES
    senha = var.EMAIL_PASSWORD

    navegador.get(
        "https://accounts.google.com/signin/v2/identifier?service=youtube")

    navegador\
        .find_element_by_xpath('//*[@id="identifierId"]')\
        .send_keys("{}".format(email))

    time.sleep(0.5)

    navegador\
        .find_element_by_xpath('//*[@id="identifierNext"]/div/button')\
        .click()

    time.sleep(2)

    navegador\
        .find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')\
        .send_keys("{}".format(senha))

    time.sleep(0.5)

    navegador\
        .find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')\
        .click()

    time.sleep(2)

    navegador.get('https://youtube.com')


if __name__ == "__main__":
    main()

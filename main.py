from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

categories = ["خرید (F1)", "فروش (F2)", "انجام شده (F4)"]


class MofidBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def Close(self):
        self.driver.close()

    def isValid(self):
        self.driver.get("https://account.emofid.com/Login")
        user_name = self.driver.find_element_by_id("Username")
        user_name.send_keys(self.username)
        user_password = self.driver.find_element_by_id("Password")
        user_password.send_keys(self.password)
        btn_submit = self.driver.find_element_by_class_name("btn-primary")
        btn_submit.click()
        try:
            self.driver.find_element_by_id("Captcha")
            return False
        except:
            return True

    def logIn(self):
        self.driver.get("https://account.emofid.com/Login")
        user_name = self.driver.find_element_by_id("Username")
        user_name.send_keys(self.username)
        user_password = self.driver.find_element_by_id("Password")
        user_password.send_keys(self.password)
        btn_submit = self.driver.find_element_by_class_name("btn-primary")
        btn_submit.click()
        self.driver.get("https://easytrader.emofid.com/")
        newVersion = self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div/a[1]"
        )
        newVersion.click()
        # TODO: ye chize dg vase load shodn kamele safhe dar nazar bgir va bezaresh tooye structure while/try
        # note: this is for the site update tag
        while True:
            try:
                self.driver.find_element_by_xpath(
                    "/html/body/app-root/d-release-notes/div/div/button"
                ).click()
                print("OK")
                break
            except:
                continue
        time.sleep(10)

    def selectedNamad(self, namad):
        k = 0
        while True:
            k += 1
            try:
                flag = self.driver.find_element_by_xpath(
                    f"/html/body/app-root/main-layout/main/div[3]/div/div/as-split/as-split-area/app-layout-selector/app-layout2/as-split/as-split-area[1]/div/as-split/as-split-area/d-portfolio-watch-container/d-market-watch/div/div[2]/div/ag-grid-angular/div/div[2]/div[1]/div[3]/div[3]/div[{k}]/div/div/span/app-symbol-state-renderer"
                )
                if flag.text == namad:
                    flag.click()
                    return True
            except:
                return False

    def kharid(self):
        btn_kharid = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/div/div/as-split/as-split-area/app-layout-selector/app-layout2/as-split/as-split-area[2]/div/div[1]/div/button[1]"
        )
        btn_kharid.click()
        _number = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/d-order-list/div/div[2]/div[1]/order-form/div/div/form/div[1]/div[1]/div/dx-number-box/div/div[1]/input"
        )
        _number.clear()
        _price = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/d-order-list/div/div[2]/div[1]/order-form/div/div/form/div[1]/div[2]/div/dx-number-box/div/div[1]/input"
        )
        _price.clear()

    def foroosh(self):
        btn_foroosh = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/div/div/as-split/as-split-area/app-layout-selector/app-layout2/as-split/as-split-area[2]/div/div[1]/div/button[2]"
        )
        btn_foroosh.click()
        _number = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/d-order-list/div/div[2]/div[1]/order-form/div/div/form/div[1]/div[1]/div/dx-number-box/div/div[1]/input"
        )
        _number.clear()
        _price = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/d-order-list/div/div[2]/div[1]/order-form/div/div/form/div[1]/div[2]/div/dx-number-box/div/div[1]/input"
        )
        _price.clear()

    def insertData(self, number, price):
        _number = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/d-order-list/div/div[2]/div[1]/order-form/div/div/form/div[1]/div[1]/div/dx-number-box/div/div[1]/input"
        )
        _number.send_keys(number)
        _price = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/d-order-list/div/div[2]/div[1]/order-form/div/div/form/div[1]/div[2]/div/dx-number-box/div/div[1]/input"
        )
        _price.send_keys(price)

    def orderNow(self):
        btn_now = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/d-order-list/div/div[2]/div[1]/order-form/div/div/form/div[3]/button[1]/span"
        )
        btn_now.click()

    def pishnevis(self):
        btn_pishnevis = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/d-order-list/div/div[2]/div[1]/order-form/div/div/form/div[3]/button[2]"
        )
        btn_pishnevis.click()

    def getTime(self):
        time = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/div/div/div/market-data/div/div[4]/easy-clock/span"
        )
        return time.text

    def maxPrice(self):
        max_price = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/d-order-list/div/div[2]/div[1]/order-form/div/div/form/div[1]/div[2]/div/div/div[1]/span[2]"
        )
        return max_price.text

    def minPrice(self):
        min_price = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/d-order-list/div/div[2]/div[1]/order-form/div/div/form/div[1]/div[2]/div/div/div[2]/span[2]"
        )
        return min_price.text

    def sendPishnevis(self):
        btn_sendAll = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/d-order-list/div/div[1]/div[2]/div/div[3]/span"
        )
        btn_sendAll.click()

    def prepare(self):
        for i in categories:
            self.driver.find_element_by_xpath(f'//span[@title="{i}"]').click()
        btn_more = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/d-order-list/div/div[1]/div[1]/div[1]/span[2]"
        )
        btn_more.click()
        btn_selectAll = self.driver.find_element_by_xpath(
            "/html/body/app-root/main-layout/main/div[3]/d-order-list/div/div[1]/div[2]/div/div[1]/small"
        )
        btn_selectAll.click()


username = ""
password = ""

test = MofidBot(username, password)

test.logIn()
test.selectedNamad(input("enter your namad: "))

# foroosh ya kharid
decision = input("kharid(K) ya foroosh(F)?! ")
if decision == "K":
    test.kharid()
else:
    test.foroosh()

number = input("tedad saham? ")
price = input("gheimat?(Max or Min) ")

if price == "Max":
    price = test.maxPrice()
elif price == "Min":
    price = test.minPrice()

print(price)

test.insertData(number, price)

# pishnevis ya now
decision = input("now(N) or pishnevis(P)? ")
time = input("what time?! ")

print(f"your input time is {time}")

if decision == "N":
    test.orderNow()
else:
    test.pishnevis()
    test.prepare()
    while time != test.getTime():
        pass
    else:
        test.sendPishnevis()

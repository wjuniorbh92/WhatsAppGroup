from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.chrome.options import Options
from time import sleep


class EnterInGroup:

    def __init__(self, group_link):
        self.group_link = group_link
        options = Options()
        self.driver = webdriver.Chrome(
            executable_path=CM().install(), options=options)

    def login(self):
        self.driver.get('https://web.whatsapp.com/')
        timeout = 100

        try:
            enter_whatsapp_web = EC.presence_of_element_located(
                (By.CLASS_NAME, "_3DJrq"))
            WebDriverWait(self.driver, timeout).until(enter_whatsapp_web)
        except TimeoutException:
            print("timeout")
        finally:
            print("Login Complete")
            return

    def enter_group(self):
        timeout = 90

        self.driver.get(self.group_link)

        click_enter_invite = EC.element_to_be_clickable(
            (By.XPATH, "//a[@id='action-button']"))
        WebDriverWait(self.driver, timeout).until(click_enter_invite).click()

        # self.driver.find_element_by_xpath("//a[@id='action-button']").click()

        enter_whatsapp_web = EC.element_to_be_clickable(
            (By.XPATH, "//div[@id='fallback_block']/div/div/a"))
        WebDriverWait(self.driver, timeout).until(enter_whatsapp_web).click()

        join_group = EC.element_to_be_clickable(
            (By.XPATH, "//div[2]/div[2]/div/div"))
        WebDriverWait(self.driver, timeout).until(join_group).click()

        try:
            full_group_await = EC.element_to_be_clickable(
                (By.XPATH, "//div[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/div/div/div"))
            WebDriverWait(self.driver, timeout).until(full_group_await)

            group_full_display = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div')
            if group_full_display.is_displayed():
                print("Group is full.")
                group_full_display.click()
                return False

        except:
            print("Looks like you joined the group.")
            self.driver.close()
            return True



print("Enter the link as in the example")
print('Just type the value after the value from chat.whatsapp.com/')
print("Example: GpYYl4uNUWmBuCr5sipj9k")
group_link = "https://chat.whatsapp.com/" + \
    input("")

whatsappbot = EnterInGroup(group_link)

whatsappbot.login()

EnterGroup = False
while EnterGroup == False:
    EnterGroup = whatsappbot.enter_group()
    sleep(240)

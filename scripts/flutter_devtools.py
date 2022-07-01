from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

btn_clear_x = 122
btn_clear_y = 105
btn_download_x = 850
btn_download_y = 105

class FlutterDevTools:
    def __init__(self, url) -> None:
        self.browser = webdriver.Chrome()
        self.actions = ActionChains(self.browser)
        self.url = url

    def open(self):
        self.browser.get(self.url)
        sleep(5)

    def click_at(self, x, y):
        elem = self.browser.find_element(by=By.TAG_NAME, value="body")
        self.actions.move_to_element_with_offset(elem, x, y).click().perform()

    def reset_frames(self):
        self.click_at(btn_clear_x, btn_clear_y)
        sleep(2)

    def export_data(self):
        self.click_at(btn_download_x, btn_download_y)
        sleep(3)

    def close(self):
        self.browser.quit()
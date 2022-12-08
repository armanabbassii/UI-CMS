from Locators import *


class Login:

    def __init__(self, driver):
        self.driver = driver

        # we set attribute in this class and we can use all functional and other thing that using from this class, we can use from this attribute

    def enter_name(self, name):
        self.driver.find_element('id', name_textbox_id).send_keys(name)

    def enter_phonenumber(self, phonenumber):
        self.driver.find_element('id', phonenumber_textbox_id).send_keys(phonenumber)

    def enter_message(self, message):
        self.driver.find_element('id', message_textbox_id).send_keys(message)

    def click_on_send_button(self):
        self.driver.find_element('class', send_button_class).click()

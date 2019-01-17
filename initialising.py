# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

try:
    from logger import logger
except ImportError as e:
    print ("Error! {}. Check if file exists".format(e))
    logger = None


class Initialising(object):

    def __init__(self, driver):
        self.driver = driver

    def setup(self):
        logger.info("Calling setUp method for {}".format(self))
        self.driver = webdriver.Chrome()
        try:
            self.driver.get("http://qa-test.klika-tech.com/")
        except Exception as err:
            logger.error("Error! {}".format(err))

    def display(self):
        try:
            field = self.driver.find_element_by_id("display")
            return field.text
        except NoSuchElementException as err:
            logger.error("Error! {}".format(err))
            exit(1)

    def find_elements(self, class_name, button):
        try:
            find_by_cls_name = self.driver.find_element_by_class_name(class_name)
            elements = find_by_cls_name.find_elements_by_tag_name("li")
            for element in elements:
                text = element.text
                if text == button:
                    element.click()
        except NoSuchElementException as err:
            logger.error("Error! {}".format(err))
            exit(1)

    def click_button(self, button):
        try:
            digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
            operations = ["C", "AC", "x", "/", "+", "-", "="]
            if button in digits:
                self.find_elements('digits', button)
            if button in operations:
                self.find_elements('operations', button)
        except NoSuchElementException as err:
            logger.error("Error! {}".format(err))

    def click_some_buttons(self, buttons):
        for button in buttons:
            self.click_button(button)

    def teardown(self):
        logger.info("Calling tearDown method for {}".format(self))
        self.driver.quit()

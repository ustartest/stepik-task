# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_btn_exist(browser):
    browser.get(link)
    try:
        is_exist = browser.find_element_by_css_selector(".btn-add-to-basket").is_displayed()
    except NoSuchElementException:
        is_exist = False
    assert is_exist is not False, "Нет кнопки Добавить в корзину"

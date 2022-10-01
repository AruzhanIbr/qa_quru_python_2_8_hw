from selene import by, be
from selene.support.shared import browser


def test_just_selene():
    browser.open('https://github.com')

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys('AruzhanIbr/qa_quru_python_2_8_hw')
    browser.element('.header-search-input').submit()

    browser.element(by.link_text('AruzhanIbr/qa_quru_python_2_8_hw')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('allure homework')).should(be.visible)


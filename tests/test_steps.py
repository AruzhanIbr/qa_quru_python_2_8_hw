import allure
from selene import by, be
from selene.support.shared import browser


def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step("Ищем репозиторий"):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').send_keys('AruzhanIbr/qa_quru_python_2_8_hw')
        browser.element('.header-search-input').submit()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text('AruzhanIbr/qa_quru_python_2_8_hw')).click()

    with allure.step("Открываем таб Issues"):
        browser.element('#issues-tab').click()

    with allure.step("Проверяем наличие Issue с названием allure homework"):
        browser.element(by.partial_text('allure homework')).should(be.visible)

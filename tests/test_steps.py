import allure
from selene import by, be
from selene.support.shared import browser


def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').send_keys('AruzhanIbr/qa_quru_python_2_8_hw')
        browser.element('.header-search-input').submit()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('AruzhanIbr/qa_quru_python_2_8_hw')).click()

    with allure.step('Открываем таб Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие Issue с названием allure homework'):
        browser.element(by.partial_text('allure homework')).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository('AruzhanIbr/qa_quru_python_2_8_hw')
    go_to_repository('AruzhanIbr/qa_quru_python_2_8_hw')
    open_issue_tab()
    should_see_issue_with_name('allure homework')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open("https://github.com")


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys(repo)
    browser.element('.header-search-input').submit()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем таб Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверяем наличие Issue с названием {name}')
def should_see_issue_with_name(name):
    browser.element(by.partial_text(name)).click()

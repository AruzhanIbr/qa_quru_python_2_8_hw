from allure_commons.types import Severity

from tests.test_steps import *


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.MINOR)
    allure.dynamic.suite('web_issue')
    allure.dynamic.label('owner', 'AruzhanIbr')
    allure.dynamic.feature('Поиск Issue')
    allure.dynamic.story('Неавторизованный пользователь может найти Issue')
    allure.dynamic.link('https://github.com', name='Testing')
    open_main_page()
    search_for_repository('AruzhanIbr/qa_quru_python_2_8_hw')
    go_to_repository('AruzhanIbr/qa_quru_python_2_8_hw')
    open_issue_tab()
    should_see_issue_with_name('allure homework')


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'AruzhanIbr')
@allure.feature('Поиск Issue')
@allure.story('Неавторизованный пользователь может найти Issue')
@allure.link('https://github.com', name='Testing')
def test_decorator_labels():
    open_main_page()
    search_for_repository('AruzhanIbr/qa_quru_python_2_8_hw')
    go_to_repository('AruzhanIbr/qa_quru_python_2_8_hw')
    open_issue_tab()
    should_see_issue_with_name('allure homework')

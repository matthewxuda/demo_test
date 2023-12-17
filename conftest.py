# -*- encoding:utf-8 -*-
from datetime import datetime

import allure
import pytest
from py.xml import html
from ui_automation.base.base_page import BasePage
from appium import webdriver
import time
@pytest.fixture(scope="session")
def login():
    print("input username, password ")
    yield
    print("clean data")
def pytest_html_report_title(report):
    report.title = "AutomationReport"
def pytest_html_results_summary(prefix, summary, postfix):
    # prefix.clear()
    prefix.extend([html.p("Department: QA")])
    prefix.extend([html.p("Owner: David")])
# th：head
# td： form
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))  # add Description
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))  # add time
    cells.pop()  #


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)

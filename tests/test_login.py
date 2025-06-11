import json
import os
import sys

import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from POM.pages.login_page import LoginPage

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'data.json'))


with open(file_path, encoding='utf-8') as f:
    test_data = json.load(f)

@pytest.mark.parametrize("case", test_data)
def test_login_scenarios(browserInstance, case):
    login_page = LoginPage(browserInstance)
    login_page.load()
    print(login_page.getTittle())
    login_page.login(case['username'],case['password'])
    message = login_page.get_message()
    browserInstance.get("https://the-internet.herokuapp.com/login")
    assert case['expected_text'] in message


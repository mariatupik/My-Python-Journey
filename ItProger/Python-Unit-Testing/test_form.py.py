import pytest
from form import Form
global_form = Form("Admin", "qwerty")

def test_form_2_param():
    assert global_form.login == "Admin"
    assert global_form.password == "qwerty"
    assert global_form.email is None
    assert global_form.url is None

def test_form_4_param():
    local_form = Form("Modest", "qwerty123", "example@gmail.com", "https://itproger.com")
    assert local_form.login == "Modest"
    assert local_form.password == "qwerty123"
    assert local_form.email == "example@gmail.com"
    assert local_form.url == "https://itproger.com"

def test_url():
    assert global_form.set_web_url("https://itprogerspd.com") is False
    assert global_form.set_web_url("https://itproger.com") is True
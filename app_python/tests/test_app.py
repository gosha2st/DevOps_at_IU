import pytest

from app import main_time

def test_not_none_response():
    assert main_time() is not None

def test_if_string_response():
    assert type(main_time()) is str

def test_center_in_response():
    assert 'center' in main_time()

# test_temp1.py

from temp1 import check_password_strength

def test_weak_passwords():
    assert check_password_strength("") == "弱"
    assert check_password_strength("abc") == "弱"
    assert check_password_strength("1234567") == "弱"
    assert check_password_strength("abcdefg") == "弱"
    assert check_password_strength("ABCDEFG") == "弱"
    assert check_password_strength("!@#$%^") == "弱"

def test_medium_passwords():
    assert check_password_strength("abcdefgh") == "中等"  # only lowercase, length>=8
    assert check_password_strength("ABCDEFGH") == "中等"  # only uppercase, length>=8
    assert check_password_strength("abcd1234") == "中等"  # lowercase + digit, length>=8
    assert check_password_strength("Abcdefgh") == "中等"  # upper + lower, length>=8
    assert check_password_strength("Abcdefg1") == "中等"  # upper + lower + digit, length>=8

def test_strong_passwords():
    assert check_password_strength("Password1!") == "強"
    assert check_password_strength("A1b2c3d4!") == "強"
    assert check_password_strength("Qwerty1!") == "強"
    assert check_password_strength("Zxcvbnm1@") == "強"

def test_edge_cases():
    assert check_password_strength("12345678") == "中等"  # only digits, length>=8
    assert check_password_strength("!!!!!!!!") == "中等"  # only special chars, length>=8
    assert check_password_strength("A!2cdefg") == "中等"  # missing one criterion
    assert check_password_strength("A1!cdefg") == "強"   # meets all criteria
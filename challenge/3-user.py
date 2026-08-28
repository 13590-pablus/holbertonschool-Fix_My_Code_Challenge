#!/usr/bin/python3
"""
User class
"""
import hashlib


class User():
    """ User class """

    def __init__(self):
        """ Constructor """
        self.__password = None

    @property
    def password(self):
        """ Password getter """
        return self.__password

    @password.setter
    def password(self, pwd):
        """ Password setter """
        if pwd is None or type(pwd) is not str:
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest()

    def is_valid_password(self, pwd):
        """ Check if pwd is valid """
        if pwd is None or type(pwd) is not str:
            return False
        if self.__password is None:
            return False
        return self.__password == hashlib.md5(pwd.encode()).hexdigest()


if __name__ == "__main__":

    print("Test User")
    user_1 = User()

    if user_1.password is not None:
        print("New User should have a None password")

    user_1.password = "My Password"

    if user_1.password is None:
        print("Just set password, so should not be None")

    if user_1.is_valid_password("My Password") is not True:
        print("is_valid_password should return True if it's the right password")

    if user_1.is_valid_password("My Password 2") is not False:
        print("is_valid_password should return False if it's not the right password")

    if user_1.is_valid_password(None) is not False:
        print("is_valid_password should return False if pwd is None")

    if user_1.is_valid_password(89) is not False:
        print("is_valid_password should return False if pwd is not a string")

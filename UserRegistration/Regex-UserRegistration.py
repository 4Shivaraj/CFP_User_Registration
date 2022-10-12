'''
    @Author: Shivaraj
    @Date: 10-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 11-10-2022
    @Title: As a User need to enter a valid Last Name
            - Last name starts with Cap and has minimum 3 characters
'''


import re
from data_log import get_logger

lg = get_logger(name="(Validate last Name)", file_name="data_log.log")


class UserRegistration:

    def __init__(self):
        """
        Container for regex pattern and valdating user input with this patterns.
        """

        self.regex_name = '^[A-Z][a-z]{2,}$'

        # last_name:            A          bc
        #                       [A-Z]      [a-z]{2,}

    def get_first_name(self, first_name):
        """
        Description:
            Takes the parameter None but return the validation of first name after matching regex pattern.
        Parameter:
            Passed parameter is None
        Return:
            Returns nothing but print the validation of first name after matching regex pattern..
        """
        try:
            matches = re.search(self.regex_name, first_name)
            if matches:
                lg.info(f'First name validated successfully: {first_name}')
            else:
                lg.info(
                    "Please re-enter the first name with name starts with capital and has minimum 3 characters")
        except Exception as e:
            lg.exception(e)

    def get_last_name(self, last_name):
        """
        Description:
            Takes the parameter None but return the validation of last name after matching regex pattern.
        Parameter:
            Passed parameter is None
        Return:
            Returns nothing but print the validation of last name after matching regex pattern..
        """
        try:
            matches = re.search(self.regex_name, last_name)
            if matches:
                lg.info(f'last name validated successfully: {last_name}')
            else:
                lg.info(
                    "Please re-enter the last name with name starts with capital and has minimum 3 characters")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    try:
        user_object = UserRegistration()

        while True:
            print(
                "Enter the choice: \n1.Validate first-name\n2.Validate last-name\n0.Exit")
            choice = int(input())
            if choice == 1:
                first_name = input("Enter the first name: ")
                user_object.get_first_name(first_name)
            elif choice == 2:
                last_name = input("Enter the last name: ")
                user_object.get_last_name(last_name)
            else:
                break
    except Exception as e:
        lg.exception(e)

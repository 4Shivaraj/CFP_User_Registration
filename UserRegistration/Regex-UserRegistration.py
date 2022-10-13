'''
    @Author: Shivaraj
    @Date: 10-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 13-10-2022
    @Title: As a User need to enter a valid First Name
            - First name starts with Cap and has minimum 3 characters
'''


import re
from data_log import get_logger

lg = get_logger(name="(Validate First Name)", file_name="data_log.log")


class UserRegistration:

    def __init__(self):
        self.regex_name = '^[A-Z][a-z]{2,}$'

        # first_name:           A          bc
        #                       [A-Z]      [a-z]{2,}

    def get_first_name(self, first_name):
        """
        Description:
            This function is used to check whether the first name starts with Cap and has minimum 3 characters
        Parameter:
            first_name: The first_name to be checked 
        Return:
            None
        """
        try:
            matches = re.search(self.regex_name, first_name)
            if matches:
                lg.info(f'First name validated successfully: {first_name}')
            else:
                lg.info("Please re-enter the first name with name starts with capital and has minimum 3 characters")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    try:
        user_object = UserRegistration()

        while True:
            print("Enter the choice: \n1.Validate first-name\n0.Exit")
            choice = int(input())
            if choice == 1:
                first_name = input("Enter the first name: ")
                user_object.get_first_name(first_name)
            else:
                break
    except Exception as e:
        lg.exception(e)

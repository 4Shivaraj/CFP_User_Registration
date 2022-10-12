'''
    @Author: Shivaraj
    @Date: 10-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 11-10-2022
    @Title: As a User need to follow pre -defined Password rules.
            Rule1   – minimum 8 Characters - 
            NOTE    – All rules must be passed
'''


import re
from data_log import get_logger

lg = get_logger(name="(Validate password rule-1)", file_name="data_log.log")


class UserRegistration:

    def __init__(self):
        """
        Container for regex pattern and valdating user input with this patterns.
        """
        self.regex_name = '^[A-Z][a-z]{2,}$'
        self.regex_email_id = '^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-z0-9-.]+$'
        self.regex_phone_no = '^[0-9]{2}\s+[6-9][0-9]{9}$'
        self.regex_password = '^[a-zA-Z0-9]{8,}$'

        # password:             shivaraj123
        #                       r'[a-zA-Z0-9]{8,}'

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

    def get_email(self, email):
        """
        Description:
            Takes the parameter None but return the validation of email id after matching regex pattern.
        Parameter:
            Passed parameter is None
        Return:
            Returns nothing but print the validation of email id after matching regex pattern.
        """
        try:
            matches = re.search(self.regex_email_id, email)
            if matches:
                lg.info(f'email validated successfully: {email}')
            else:
                lg.info(
                    "Please re-enter the valid email")
        except Exception as e:
            lg.exception(e)

    def get_phone_number(self, phone_num):
        """
        Description:
            Takes the parameter None but return the validation of phone number after matching regex pattern.
        Parameter:
            Passed parameter is None
        Return:
            Returns nothing but print the validation of phone number after matching regex pattern.
        """
        try:
            matches = re.search(self.regex_phone_no, phone_num)
            if matches:
                lg.info(f'Phone number validated successfully: {phone_num}')
            else:
                lg.info(
                    "Please re-enter the valid phone number")
        except Exception as e:
            lg.exception(e)

    def get_password(self, password):
        """
        Description:
            Takes the parameter None but return the validation of password after matching regex pattern.
        Parameter:
            Passed parameter is None
        Return:
            Returns nothing but print the validation of password after matching regex pattern.
        """
        try:
            matches = re.search(self.regex_password, password)
            if matches:
                lg.info(f'Password validated successfully: {password}')
            else:
                lg.info(
                    "Please re-enter the valid password")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    try:
        user_object = UserRegistration()

        while True:
            print("Enter the choice: \n1.Validate first-name\n2.Validate last-name\n3.Validate email-id\n4.Validate Phone number\n5.Validate password\n0.Exit")
            choice = int(input())
            if choice == 1:
                first_name = input("Enter the first name: ")
                user_object.get_first_name(first_name)
            elif choice == 2:
                last_name = input("Enter the last name: ")
                user_object.get_last_name(last_name)
            elif choice == 3:
                email = input("Enter the email id: ")
                user_object.get_email(email)
            elif choice == 4:
                phone_num = input("Enter the phone number: ")
                user_object.get_phone_number(phone_num)
            elif choice == 5:
                password = input("Enter the password: ")
                user_object.get_password(password)
            else:
                break
    except Exception as e:
        lg.exception(e)

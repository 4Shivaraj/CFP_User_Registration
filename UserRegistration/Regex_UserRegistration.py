'''
    @Author: Shivaraj
    @Date: 10-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 13-10-2022
    @Title: Should clear all email samples provided separately
'''

import re
from data_log import get_logger

lg = get_logger(name="(For Test Case)", file_name="data_log.log")


class UserRegistration:
    def __init__(self):
        self.regex_name = '^[A-Z][a-z]{2,}$'
        self.regex_email_id = '^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-z0-9-.]+$'
        self.regex_phone_no = '^[0-9]{2}\s+[6-9][0-9]{9}$'
        self.regex_password = '^(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{7,}[!@#$%^&*()_+=|\{};:"?/.<>,]{1}$'
        self.regex_email_samples = '^[a-zA-Z0-9]+([._+-][a-zA-Z0-9]{2,})*@[a-zA-Z0-9]{1,}\.[a-zA-Z]{2,4}(\.[a-zA-z]{' \
                                   '2,3})?$ '

        # email_samples:
        # abc             .100                        @abc                .com                .au r'[
        # a-zA-Z0-9]   +([._+-][a-zA-Z0-9]{2,})    *@[a-zA-Z0-9]{1,}   \.[a-zA-Z]{2,4}     (\.[a-zA-z]{2,3})?

    def get_first_name(self, first_name):
        """
        Description:
             This function is used to check whether the first name starts with Cap and has minimum 3 characters
        Parameter:
            first_name: The first_name to be checked
        Return:
            Returns first_name if its valid else returns False
        """
        try:
            matches = re.search(self.regex_name, first_name)
            if matches:
                return first_name
            else:
                return False
        except Exception as e:
            lg.exception(e)

    def get_last_name(self, last_name):
        """
        Description:
            This function is used to check whether the last name starts with Cap and has minimum 3 characters
        Parameter:
            last_name: The last_name to be checked
        Return:
            Returns last_name if its valid else returns False
        """
        try:
            matches = re.search(self.regex_name, last_name)
            if matches:
                return last_name
            else:
                return False
        except Exception as e:
            lg.exception(e)

    def get_email(self, email):
        """
        Description:
            This function is used to check for valid email
        Parameter:
            email: The email to be checked
        Return:
            Returns email if its valid else returns False
        """
        try:
            matches = re.search(self.regex_email_id, email)
            if matches:
                return email
            else:
                return False
        except Exception as e:
            lg.exception(e)

    def get_phone_number(self, phone_num):
        """
        Description:
            This function is used to check for valid phone number
        Parameter:
            phone_num: The phone_num to be checked
        Return:
            Returns phone_num if its valid else returns False
        """
        try:
            matches = re.search(self.regex_phone_no, phone_num)
            if matches:
                return phone_num
            else:
                return False
        except Exception as e:
            lg.exception(e)

    def get_password(self, password):
        """
        Description:
            This function is used to check for valid password
        Parameter:
            password: The password to be checked
        Return:
            Returns password if its valid else returns False
        """
        try:
            matches = re.search(self.regex_password, password)
            if matches:
                return password
            else:
                return False
        except Exception as e:
            lg.exception(e)

    def get_email_samples(self, email_samples):
        """
        Description:
            This function is used to check for valid email samples
        Parameter:
            email_samples: The email_samples to be checked
        Return:
            Returns email_samples if its valid else returns False
        """
        try:
            matches = re.search(self.regex_email_samples, email_samples)
            if matches:
                return email_samples
            else:
                return False
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    try:
        user_object = UserRegistration()

        while True:
            print("Enter the choice: \n1.Validate first-name\n2.Validate last-name\n3.Validate email-id\n4.Validate "
                  "Phone number\n5.Validate password\n6.Validate email samples\n0.Exit")
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
            elif choice == 6:
                valid_email = ['abc@yahoo.com', 'abc-100@yahoo.com', 'abc.100@yahoo.com', 'abc111@abc.com',
                               'abc-100@abc.net', 'abc.100@abc.com.au', 'abc@1.com', 'abc@gmail.com.com',
                               'abc+100@gmail.com']
                invalid_email = ['abc', 'abc@.com.my', 'abc123@gmail.a', 'abc123@.com', 'abc123@.com.com',
                                 '.abc@abc.com',
                                 'abc()\* @gmail.com', 'abc@%\*.com', 'abc..2002@gmail.com', 'abc.@gmail.com',
                                 'abc@abc@gmail.com', 'abc@gmail.com.1a', 'abc@gmail.com.aa.au']
                print('List of valid emails')
                for email in valid_email:
                    user_object.get_email_samples(email)

                print('List of in-valid emails')
                for email in invalid_email:
                    user_object.get_email_samples(email)
            else:
                break
    except Exception as e:
        lg.exception(e)

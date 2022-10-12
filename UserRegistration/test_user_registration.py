'''
    @Author: Shivaraj
    @Date: 10-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 11-10-2022
    @Title: Unit testing of test cases for user registration
'''

import unittest
from Regex_UserRegistration import UserRegistration


user_obj = UserRegistration()


class TestUserRegistration(unittest.TestCase):
    # start with capital letter and minimum 3 chars.
    def test_to_validate_first_name(self):
        self.assertTrue(user_obj.get_first_name('Shiva'))
        self.assertFalse(user_obj.get_first_name('shiva'))
        self.assertTrue(user_obj.get_first_name('Shi'))
        self.assertFalse(user_obj.get_first_name('Sh'))
        self.assertEqual(user_obj.get_first_name('Shivaraj'), 'Shivaraj')
        self.assertNotEqual(user_obj.get_first_name('Shivaraj'), 'shivaraj')

    # start with capital letter and minimum 3 chars.
    def test_to_validate_last_name(self):
        self.assertTrue(user_obj.get_last_name('Gowda'))
        self.assertFalse(user_obj.get_last_name('gowda'))
        self.assertTrue(user_obj.get_last_name('Gow'))
        self.assertFalse(user_obj.get_last_name('Go'))
        self.assertEqual(user_obj.get_last_name('Krish'), 'Krish')
        self.assertNotEqual(user_obj.get_last_name('Gowda'), 'gowda')

    # Email has 3 mandatory parts (abc, bl & co) and 2 optional (xyz & in) with precise @ and . positions
    def test_to_validate_email(self):
        self.assertTrue(user_obj.get_email('abc.xyz@bl.co.in'))
        self.assertFalse(user_obj.get_email('.xyzbl.co.in'))
        self.assertTrue(user_obj.get_email('abc.@bl.co.in'))
        self.assertFalse(user_obj.get_email('abc.xyz@.co.in'))
        self.assertTrue(user_obj.get_email('abc@bl.co'))
        self.assertFalse(user_obj.get_email('abc@bl'))
        self.assertEqual(user_obj.get_email(
            'abc.xyz@bl.co.in'), 'abc.xyz@bl.co.in')
        self.assertNotEqual(user_obj.get_email(
            '4shivaraj.gowda@gmail.com'), '4shivarajgowda@gmail.com')

    # Country code followed by 10 digit phone number
    def test_to_validate_phone_number(self):
        self.assertTrue(user_obj.get_phone_number('91 8618199770'))
        self.assertFalse(user_obj.get_phone_number('8618199770'))
        self.assertTrue(user_obj.get_phone_number('91 6350789669'))
        self.assertFalse(user_obj.get_phone_number('861819'))
        self.assertFalse(user_obj.get_phone_number('91 4789267892'))
        self.assertEqual(user_obj.get_phone_number(
            '91 8618199772'), '91 8618199772')
        self.assertNotEqual(user_obj.get_phone_number(
            '91 8618199771'), '918618199771')
        self.assertEqual(len(user_obj.get_phone_number('91 8618199771')), 13)
        self.assertNotEqual(
            len(user_obj.get_phone_number('91 8618199771')), 10)

    # Password should be minimum 8 char, at least 1 upper char, atleast 1 numeric num, exactly one special char
    def test_to_validate_password(self):
        self.assertTrue(user_obj.get_password('Shiva123@'))
        self.assertFalse(user_obj.get_password('shivaraj'))
        self.assertFalse(user_obj.get_password('Shivaraj'))
        self.assertFalse(user_obj.get_password('shivaraj12'))
        self.assertFalse(user_obj.get_password('Shiva123@!'))
        self.assertFalse(user_obj.get_password('Gan123@'))
        self.assertEqual(len(user_obj.get_password('Gana123@')), 8)
        self.assertTrue(user_obj.get_password('Ganu123@'), 'Ganu123@')
        self.assertNotEqual(user_obj.get_password('Ganu123@'), 'Ganu123@!')

    # Valid email samples
    def test_to_validate_valid_email_samples(self):
        self.assertTrue(user_obj.get_email_samples('abc@yahoo.com'))
        self.assertTrue(user_obj.get_email_samples('abc-100@yahoo.com'))
        self.assertTrue(user_obj.get_email_samples('abc.100@yahoo.com'))
        self.assertTrue(user_obj.get_email_samples('abc111@abc.com'))
        self.assertTrue(user_obj.get_email_samples('abc100@abc.com'))
        self.assertTrue(user_obj.get_email_samples('abc.100@abc.com.au'))
        self.assertTrue(user_obj.get_email_samples('abc@1.com'))
        self.assertTrue(user_obj.get_email_samples('abc@gmail.com.com'))
        self.assertTrue(user_obj.get_email_samples('abc+100@gmail.com'))

    # Invalid email samples
    def test_to_validate_invalid_email_samples(self):
        self.assertFalse(user_obj.get_email_samples('abc'))
        self.assertFalse(user_obj.get_email_samples('abc@.com.my'))
        self.assertFalse(user_obj.get_email_samples('abc123@gmail.a'))
        self.assertFalse(user_obj.get_email_samples('abc123@.com'))
        self.assertFalse(user_obj.get_email_samples('abc123@.com.com'))
        self.assertFalse(user_obj.get_email_samples('.abc@abc.com'))
        self.assertFalse(user_obj.get_email_samples('abc()\* @gmail.com'))
        self.assertFalse(user_obj.get_email_samples('abc@%\*.com'))
        self.assertFalse(user_obj.get_email_samples('abc.@gmail.com'))
        self.assertFalse(user_obj.get_email_samples('abc@abc@gmail.com'))
        self.assertFalse(user_obj.get_email_samples('abc@gmail.com.1a'))
        self.assertFalse(user_obj.get_email_samples('abc@gmail.com.aa.au'))


if __name__ == '__main__':
    unittest.main()

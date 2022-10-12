User Registration
User Registration System needs to ensure all validations are in place during the User Entry

1. As a User need to enter a valid First Name

   - First name starts with Cap and has minimum 3 characters

2. As a User need to enter a valid Last Name

   - Last name starts with Cap and has minimum 3 characters

3. As a User need to enter a valid email

   - E.g. abc.xyz@bl.co.in - Email has 3 mandatory parts (abc, bl & co)
     and 2 optional (xyz & in) with precise @ and . positions

4. As a User need to follow pre-defined Mobile Format

   - E.g. 91 9919819801 - Country code follow by space and 10 digit number

5. As a User need to follow pre -defined Password rules.

   Rule1 – minimum 8 Characters -
   NOTE – All rules must be passed

6. Rule2 – Should have at least 1 Upper Case
   NOTE – All rules must be passed

7. Rule3 – Should have at least 1 numeric number in the password
   NOTE – All rules must be passed

8. Rule4 – Has exactly 1 Special Character

   - NOTE – All rules must be passed

9. Should clear all email samples provided separately

• A. Valid Emails
• 1. abc@yahoo.com,
• 2. abc-100@yahoo.com,
• 3. abc.100@yahoo.com
• 2. abc111@abc.com,
• 4. abc-100@abc.net,
• 5. abc.100@abc.com.au
• 6. abc@1.com,
• 7. abc@gmail.com.com
• 8. abc+100@gmail.com

B. Invalid Emails (TLD - Top Level Domains)

1. abc – must contains “@” symbol
2. abc@.com.my – tld can not start with dot “.”
3. abc123@gmail.a – “.a” is not a valid tld, last tld must contains at least two
   characters
4. abc123@.com – tld can not start with dot “.”
5. abc123@.com.com – tld can not start with dot “.”
6. .abc@abc.com – email’s 1st character can not start with “.”
7. abc()\*@gmail.com – email’s is only allow character, digit, underscore and dash
8. abc@%\*.com – email’s tld is only allow character and digit
9. abc..2002@gmail.com – double dots “.” are not allow
10. abc.@gmail.com – email’s last character can not end with dot “.”
11. abc@abc@gmail.com – double “@” is not allow
12. abc@gmail.com.1a -email’s tld which has two characters can not contains digit
13. abc@gmail.com.aa.au - cannont have multiple email’s tld

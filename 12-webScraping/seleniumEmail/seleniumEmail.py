#! python3
# seleniumEmail.py - python script to draft an email from text provided on the command line

from selenium import webdriver
import sys, re

if len(sys.argv) < 1:
    print("Please provide valie Email address and message to be sent...")

else:
    # Create email Regex
    emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)
    
    email = emailRegex.findall(sys.argv[1])[0][0]
    message = ' '.join(sys.argv[2:])

    if email and len(message) > 0:
        print(f'Sending: \n {message}')
        print(f'To: {email}')

        browser = webdriver.Firefox()
        browser.get('https://mail.google.com')
    


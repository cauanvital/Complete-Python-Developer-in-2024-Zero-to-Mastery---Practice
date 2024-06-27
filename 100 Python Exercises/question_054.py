# Assuming that we have some email addresses in the "username@companyname.com"
# format, please write program to print the company name of a given email
# address. Both user names and company names are composed of letters only.
# 
# Example: If the following email address is given as input to the program:
#   john@google.com
# 
# Then, the output of the program should be:
#   google
# 
# In case of input data being supplied to the question, it should be assumed to
# be a console input.

email = input()

def get_username(email:str):
    company_start = email.find('@') + 1
    company_end = email.rfind('.')
    return email[company_start:company_end]

print(get_username(email))

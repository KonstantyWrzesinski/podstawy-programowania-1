###
# A program that checks whether the password length
# read from the keyboard is correct.
#
password = input('Enter password: ')
password_ok = len(password) >= 8
if password_ok:
    print('pasword ok')
else:
    print('pasword to short')
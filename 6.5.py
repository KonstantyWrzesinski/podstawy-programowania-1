###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
phone_num =''
i=0
for i in range(9):
    phone_num+=phone[i]
    if (i+1)%3 == 0 and i!=8:
        phone_num+='-'
print(phone_num)
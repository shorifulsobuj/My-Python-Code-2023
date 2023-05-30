print('-------------------')
email = input('set email: ')
password = input('set password: ')

print('login using your email and password')
print('-------------------------------------')

loginEmail = input('email>> ')
loginpass = input('password>> ')

if(email==loginEmail and password==loginpass):
    print(f'Hi, {email}, You login successful')
else:
    print(f'Hi, {email}, You login Unsuccessful')
# This program Explains about the elif in python


print('Please Enter your Name : ')
MyName = input()
print('Please Enter your age : ')
MyAge = input()
print('Enter Your Company Name:')
CompanyName = input()
print('Enter your location ')
MyLocation = input()

if MyName == 'vasanth':
    print('Welcome Boss!!!')
elif MyAge >= 27:
    print('Access Granted but not Full Access')
elif CompanyName == 'kgisl':
    print('Access granted for particular time ')
elif MyLocation == 'coimbatore':
    print('Access is granted for now !!!')
else:
    print('Access Denied !!!')

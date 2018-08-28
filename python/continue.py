# This is the Simple Example of Break Statement

while True :
    print('Please Enter your name : ')
    name = input()

    if name != 'joe':   
        continue
    print('please Enter Your Password :')
    passw = input()

    if passw == '8888':
        print('Welcome Boss!!')
        print('Access Granted ')
        break
print('Good day')

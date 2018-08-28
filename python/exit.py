# This is the Example of Exit function in python

import sys

while True:
    print('Type Exit to Exit the application')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You are Exited From the application')

from messages import *
from colors import *
from initial_data import *
from core import *

send_message('Hello Message')
text = str.upper(input())

if text == 'ABC':  # the program will write all the characters it can write
    text = test_text
    main_action(text)
elif text == 'COLORTEST':  # the program will show a color test
    color_test()
else:
    main_action(text)


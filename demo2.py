from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
m = PyMouse()
k = PyKeyboard()
dely_time = 1
while dely_time < 5:
    k.press_key(k.alt_key)
    k.release_key(k.alt_key)
    time.sleep(10)    
    key_word = input()
    print ('input your exit word:', key_word)
    if key_word == '1':
        break
    else:
        print('This demo is running，',dely_time,'round')
        print('Do you want to stop this demo?')
    dely_time+=1
import os
try:
    x = os.system('xdg-open https://g.co/kgs/8iehEi')
    if x == 0:
        os.system('chmod 777 f')
        os.system('python fire.py')
except:
    exit(' use 64bit for executing this  ')

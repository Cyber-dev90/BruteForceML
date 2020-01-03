import os,time
print('Menginstall Packet',end='\r')
for i in range(10):
    print('.',end='\r')
    time.sleep(0.5)
os.system('pip install yagmail')
os.system('pip install termcolor')
os.system('pkg install figlet')

import yagmail
from termcolor import colored


print(colored('Packet Selesai Di Install','green'))
os.system('sleep 3')
os.system('python ml.py')

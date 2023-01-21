from os import system
from datetime import datetime
from core import profile, extend
from time import sleep

c = '\x1b[38;5;45m'
o = '\x1b[38;5;208m'
h = '\x1b[38;5;40m'
p = '\x1b[38;5;253m'
p2 = '\x1b[38;5;204m'
date = datetime.now().strftime('%d-%m-%Y')
akun = []

def login():
    system('clear')
    try:
        akun.append(open('.kuk','r').read())
        yanto = extend.yantogeming(akun[0])
        if 'invalid' in str(yanto):
            system('rm .kuk')
            exit('Invalid Cookies')
        else:
            home(yanto)
    except FileNotFoundError:
        print(f'{p}Merch Facebook Toolkit For Free')
        print(f'{p}Jangan Buat Yang Aneh Aneh, Dosa Tanggung Sendiri')
        kukis = input(f'\n{p}Cookies: {h}')
        ext = extend.yantogeming(kukis)
        if 'invalid' in str(ext):
            print('Invalid Cookies')
        else:
            akun.append(kukis)
            open('.kuk','w').write(kukis)
            home(ext)

    
def home(nama):
    system('clear')
    print(f'''
{p2} __  __ {p} ____ _____  ____  _   _   {p2}  ____ {p}_____  _____ 
{p2}|  \/  |{p}| ===|| () )/ (__`| |_| |  {p2} | ===|{p}| () )|_   _|
{p2}|_|\/|_|{p}|____||_|\_\\\____)|_| |_| {p2}  |__| {p} |_()_)  |_|  
 Login Sebagai:{c} {nama}
 {p}Date:{c} {date}

 {p2}No).{p} Tools Name
 --------------------------------
{p2} 01).{p} Bot React All Post Friends
{p2} 02).{p} Bot Comment All Post Friends
{p2} 00).{p} Logout And Remove Cookies
 ''')
    ch = input(f' {p}??).{p} Chose Number: {h}')
    if ch == '1' or ch == '01':
        print(f'\n {p2}$$).{p} Enter Friends ID or Ussername')
        fid = input(f'{p} Fid: {c}')
        print(f'''\n {p2}No).{p} React Actions
--------------------------------
{p2} 01).{p} Like
{p2} 02).{p} Super
{p2} 03).{p} Peduli
{p2} 04).{p} Haha
{p2} 05).{p} Wow
{p2} 06).{p} Sedih
{p2} 07).{p} Marah
        ''')
        xc = input(f'\n {p}??). Chose Number:{h} ')
        print('')
        if xc == '1' or xc == '01':
            profile.react_profile(fid, 0, akun[0])
        elif xc == '2' or xc == '02':
            profile.react_profile(fid, 1, akun[0])
        elif xc == '3' or xc == '03':
            profile.react_profile(fid, 2, akun[0])
        elif xc == '4' or xc == '04':
            profile.react_profile(fid, 3, akun[0])
        elif xc == '5' or xc == '05':
            profile.react_profile(fid, 4, akun[0])
        elif xc == '6' or xc == '06':
            profile.react_profile(fid, 5, akun[0])
        elif xc == '7' or xc == '07':
            profile.react_profile(fid, 6, akun[0])
    elif ch == '2' or ch == '02':
        print(f'\n {p2}$$).{p} Enter Friends ID or Ussername')
        fid = input(f'{p} Fid: {c}')
        msg = input(f'{p} Message: {o}')
        print('')
        profile.comment_profile(fid, msg, akun[0])
    elif ch == '0' or ch == '00':
        system('rm .kuk')
        exit()
    else:
        print(f' {o}Number Not Found')
        sleep(3)
        home(nama)
            

if __name__=='__main__':
    system('git pull')
    login()

from os import system
from datetime import datetime
from core import core_vanz
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
        core_vanz.login(akun[0])
        st = open('.st','r').read()
        if st == 'val':
            print(f'{p}Cookies Invalid')
            system('rm .kuk')
        else:
            home(st)
    except FileNotFoundError:
        print(f'{p}Merch Facebook Toolkit For Free')
        print(f'{p}Jangan Buat Yang Aneh Aneh, Dosa Tanggung Sendiri')
        print(f'{p}Gunakan Sewajarnya Saja, Kalo Cp Bukan Tanggung Jawab Author')
        kukis = input(f'\n{p}Cookies: {h}')
        core_vanz.login(kukis)
        st = open('.st','r').read()
        if st == 'val':
            print(f'{p}Invalid Cookies')
        else:
            akun.append(kukis)
            open('.kuk','w').write(kukis)
            home(st)

    
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
        xc = input(f' {p}??). Chose Number:{h} ')
        print(f'\n{p} User ( CTRL + Z ) For Stop Program...')
        if xc == '1' or xc == '01':
            core_vanz.react_profile(fid, 0, akun[0])
        elif xc == '2' or xc == '02':
            core_vanz.react_profile(fid, 1, akun[0])
        elif xc == '3' or xc == '03':
            core_vanz.react_profile(fid, 2, akun[0])
        elif xc == '4' or xc == '04':
            core_vanz.react_profile(fid, 3, akun[0])
        elif xc == '5' or xc == '05':
            core_vanz.react_profile(fid, 4, akun[0])
        elif xc == '6' or xc == '06':
            core_vanz.react_profile(fid, 5, akun[0])
        elif xc == '7' or xc == '07':
            core_vanz.react_profile(fid, 6, akun[0])
        else:
            print(f' {o}Number Not Found')
            sleep(3)
            home(nama)
    elif ch == '2' or ch == '02':
        print(f'\n {p2}$$).{p} Enter Friends ID or Ussername')
        fid = input(f'{p} Fid: {c}')
        msg = input(f'{p} Message: {o}')
        print(f'\n{p} Use ( CTRL + Z ) For Stop Program...')
        profile.comment_profile(fid, msg, akun[0])
    # elif ch == '3' or ch == '03':
        # print(f'\n {p2}$$).{p} Enter ID or Ussername Public Users')
        # pid = input(f'{p} Pid: {c}')
        # add_friends.add_friends(pid, akun[0])
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

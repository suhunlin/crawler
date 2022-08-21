from datetime import datetime, timedelta
from crawler.futures.futures_crawler import FuturesCrawler

def main():
    url = 'https://www.taifex.com.tw/cht/3/futContractsDate'
    date = datetime.today()
    f1 = FuturesCrawler(url, date)
    f1.futures_http_get()



if __name__ == '__main__':
    main()
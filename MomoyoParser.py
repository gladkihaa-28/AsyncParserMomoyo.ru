import asyncio
import csv
import time
import aiohttp as aiohttp
from bs4 import BeautifulSoup
from itertools import zip_longest
import requests

start_time = time.time()

a = int(input('Введите от (если запускаете в первый раз, введите 1: '))
file = input('Введите название файла: ')

cookies = {
    '_ym_uid': '1680011460304066752',
    '_ym_d': '1680011460',
    'antibot_01a5dc6d14684504e28df008953912e5': 'cf0471b987c6feebc3f215337a590dfc-1685084268',
    'START_HTTP_REFERER': '-',
    'START_REQUEST_URI': '-',
    '_ym_isad': '2',
    '_gid': 'GA1.2.1130952510.1685084271',
    '_gat_gtag_UA_149403361_1': '1',
    '_ym_visorc': 'w',
    'antibot_hits': '3',
    'START_TIME': '1685084283',
    '_ga_EMQNBWH0BD': 'GS1.1.1685084271.1.1.1685084283.0.0.0',
    '_ga': 'GA1.1.1664759585.1685084271',
}
headers = {
    'authority': 'momoyo.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_ym_uid=1680011460304066752; _ym_d=1680011460; antibot_01a5dc6d14684504e28df008953912e5=cf0471b987c6feebc3f215337a590dfc-1685084268; START_HTTP_REFERER=-; START_REQUEST_URI=-; _ym_isad=2; _gid=GA1.2.1130952510.1685084271; _gat_gtag_UA_149403361_1=1; _ym_visorc=w; antibot_hits=3; START_TIME=1685084283; _ga_EMQNBWH0BD=GS1.1.1685084271.1.1.1685084283.0.0.0; _ga=GA1.1.1664759585.1685084271',
    'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
}

cookies1 = {
    '_ym_uid': '1680011460304066752',
    '_ym_d': '1680011460',
    'antibot_01a5dc6d14684504e28df008953912e5': 'cf0471b987c6feebc3f215337a590dfc-1685084268',
    'START_HTTP_REFERER': '-',
    'START_REQUEST_URI': '-',
    '_ym_isad': '2',
    '_gid': 'GA1.2.1130952510.1685084271',
    '_gat_gtag_UA_149403361_1': '1',
    '_ym_visorc': 'w',
    'antibot_hits': '4',
    'START_TIME': '1685084293',
    '_ga_EMQNBWH0BD': 'GS1.1.1685084271.1.1.1685084294.0.0.0',
    '_ga': 'GA1.2.1664759585.1685084271',
}
headers1 = {
    'authority': 'momoyo.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    # 'cookie': '_ym_uid=1680011460304066752; _ym_d=1680011460; antibot_01a5dc6d14684504e28df008953912e5=cf0471b987c6feebc3f215337a590dfc-1685084268; START_HTTP_REFERER=-; START_REQUEST_URI=-; _ym_isad=2; _gid=GA1.2.1130952510.1685084271; _gat_gtag_UA_149403361_1=1; _ym_visorc=w; antibot_hits=4; START_TIME=1685084293; _ga_EMQNBWH0BD=GS1.1.1685084271.1.1.1685084294.0.0.0; _ga=GA1.2.1664759585.1685084271',
    'referer': 'https://momoyo.ru/m216',
    'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
}

r = requests.get('https://momoyo.ru/m1708', cookies=cookies, headers=headers).text
soup = BeautifulSoup(r, 'lxml')
lim = int(int(soup.find('p', class_='gcnt').text.split()[1]) / 100) + 1
print(lim)
for r in range(a, lim):
    async def card(link):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://momoyo.ru{link}', cookies=cookies1, headers=headers1) as resp:
                    sp = []
                    body = await resp.text()
                    soup = BeautifulSoup(body, 'lxml')
                    name = soup.find('h1').text
                    ph = soup.find('a', class_='pointer outli').find('img').get('src')
                    for tags in soup.find_all('p', class_='details'):
                        if 'Производитель:' in tags.text:
                            pr = tags.text.split()[1:]
                            pr = " ".join(pr)
                        if 'Штрих-код:' in tags.text:
                            bar = tags.text.split()[1]
                    l = [r]
                    list1 = [name]
                    list2 = [pr]
                    k = [ph]
                    list3 = [bar]
                    d = [l, list1, list2, k, list3]
                    export_data = zip_longest(*d, fillvalue='')
                    with open(f'{file}.csv', 'a', encoding="utf-8", newline='') as myfile:
                        wr = csv.writer(myfile, delimiter=';')
                        wr.writerows(export_data)
                        sp.clear()
                    print(name)
        except:
            print('Error')


    async def scrape(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, cookies=cookies, headers=headers) as resp:
                body = await resp.text()
                soup = BeautifulSoup(body, 'lxml')
                for l1 in soup.find_all('div', class_='name'):
                    l = l1.find('a').get('href')
                    await card(l)



    async def main():




        tasks = []
        urls = []
        y = (r - 1) * 100
        x = r * 100
        for i in range(y + 1, x):
            print(i)
            task = asyncio.create_task(scrape(f'https://momoyo.ru/m1708/page{i}'))
            tasks.append(task)

        print('Saving the output of extracted information')
        await asyncio.gather(*tasks)




    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

time_difference = time.time() - start_time
print(f'Scraping time: %.2f seconds.' % time_difference)
import requests
from bs4 import BeautifulSoup
from pyppeteer import launch
import asyncio


def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height


async def main(url):
    browser = await launch({'headless': False, 'args': ['--no-sandbox'], 'executablePath': 'C:\\zhenxin\\chrome-win\\chrome.exe',})
    # browser = await launch({'args': ['--no-sandbox'], })
    page = await browser.newPage()
    width, height = screen_size()
    await page.setViewport(viewport={"width": width, "height": height})
    await page.setJavaScriptEnabled(enabled=True)
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
    )
    await page.goto(url)

    # await asyncio.sleep(2)

    await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')

    await asyncio.sleep(1)

    # content = await page.content()
    li_list = await page.xpath('//*[@id="J_goodsList"]/ul/li')

    # print(li_list)
    item_list = []
    for li in li_list:
        a = await li.xpath('.//div[@class="p-img"]/a')
        detail_url = await (await a[0].getProperty("href")).jsonValue()
        promo_words = await (await a[0].getProperty("title")).jsonValue()
        a_ = await li.xpath('.//div[@class="p-commit"]/strong/a')
        p_commit = await (await a_[0].getProperty("textContent")).jsonValue()
        i = await li.xpath('./div/div[3]/strong/i')
        price = await (await i[0].getProperty("textContent")).jsonValue()
        em = await li.xpath('./div/div[4]/a/em')
        title = await (await em[0].getProperty("textContent")).jsonValue()
        item = {
            "title": title,
            "detail_url": detail_url,
            "promo_words": promo_words,
            'p_commit': p_commit,
            'price': price
        }
        item_list.append(item)
        # print(item)
        # break
    # print(content)

    await page_close(browser)
    return item_list


async def page_close(browser):
    for _page in await browser.pages():
        await _page.close()
    await browser.close()


msg = "手机"
url = "https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={}&cid2=653&cid3=655&page={}"

task_list = []
for i in range(1, 2):
    page = i * 2 - 1
    url = url.format(msg, msg, page)
    task_list.append(main(url))

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(*task_list))
# print(results, len(results))
for i in results:
    print(i, len(i))

print('*' * 100)
# soup = BeautifulSoup(content, 'lxml')
# div = soup.find('div', id='J_goodsList')
# for i, li in enumerate(div.find_all('li', class_='gl-item')):
#     if li.select('.p-img a'):
#         print(li.select('.p-img a')[0]['href'], i)
#         print(li.select('.p-price i')[0].get_text(), i)
#         print(li.select('.p-name em')[0].text, i)
#     else:
#         print("#" * 200)
#         print(li)
import asyncio
import parsel

from pyppeteer import launch


async def main():
    exe_path = 'C:\\zhenxin\\chrome-win\\chrome.exe'
    browser = await launch({'executablePath': exe_path,
                            'headless': False})
    page = await browser.newPage()
    await page.goto('http://quotes.toscrape.com/js/')
    page_text = await page.content()
    selector = parsel.Selector(page_text)
    div_list = selector.xpath('//div[@class="quote"]')
    print(len(div_list))
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())

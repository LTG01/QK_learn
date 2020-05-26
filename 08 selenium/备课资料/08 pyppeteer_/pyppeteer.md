### 环境安装

第三方库下载

```
pip install pyppeteer 
```

驱动下载

在这里使用的是淘宝镜像中的 chromium 
进入这个网址 https://npm.taobao.org/mirrors/chromium-browser-snapshots

下载后解答到一个文件夹

### 快速上手 

Pyppeteer 是一款非常高效的 web 自动化测试工具，由于 Pyppeteer 是基于 asyncio 构建的，它的所有 属性 和方法 几乎都是 coroutine (协程) 对象，因此在构建异步程序的时候非常方便，天生就支持异步运行。

程序构建的基本思路是新建 一个 browser 浏览器 和 一个 页面 page。

看下面这段代码，在 main 函数中，先是建立一个浏览器对象，然后打开新的标签页，访问百度主页，对当前页面截图并保存为“example.png”，最后关闭浏览器。pyppeteer 是基于 asyncio 构建的，所以在使用的时候需要用到 async/await 结构。

```
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
```

launch 方法会新建一个 Browser 对象，然后赋值给 browser。再创建的过程中可以指定一些参数。

因为 Pyppeteer 默认使用的是无头浏览器，如果想要浏览器显示，需要在launch 函数中设置参数 “headless =False”

调用 newPage 方法相当于浏览器中新建了一个选项卡，同时新建了一个 Page 对象。

然后 Page 对象调用了 goto 方法就相当于在浏览器中输入了这个 URL，浏览器跳转到了对应的页面进行加载，加载完成之后再调用 content 方法，返回当前浏览器页面的源代码。

然后用 parsel 进行同样地解析，就可以得到 JavaScript 渲染的结果了。在这个过程中，我们没有配置 Chrome 浏览器，没有配置浏览器驱动，免去了一些繁琐的步骤，同样达到了 Selenium 的效果，还实现了异步抓取。

### 详情用法

- 开启浏览器

  - 调用 launch 方法即可，相关参数介绍：
    - ignoreHTTPSErrors (bool): 是否要忽略 HTTPS 的错误，默认是 False。
    - headless (bool): 是否启用 Headless 模式，即无界面模式，如果 devtools 这个参数是 True 的话，那么该参数就会被设置为 False，否则为 True，即默认是开启无界面模式的。
    - executablePath (str): 可执行文件的路径，如果指定之后就不需要使用默认的 Chromium 了，可以指定为已有的 Chrome 或 Chromium。
    - args (List[str]): 在执行过程中可以传入的额外参数。
    - devtools (bool): 是否为每一个页面自动开启调试工具，默认是 False。如果这个参数设置为 True，那么 headless 参数就会无效，会被强制设置为 False。

- 关闭提示条：”Chrome 正受到自动测试软件的控制”，这个提示条有点烦，那咋关闭呢？这时候就需要用到 args 参数了，禁用操作如下：

  ```
   browser = await launch(headless=False, args=['--disable-infobars'])
  ```

- 处理页面显示问题:访问淘宝首页

```
import asyncio
from pyppeteer import launch


async def main():
    exe_path = 'C:\\zhenxin\\chrome-win\\chrome.exe'
    browser = await launch({'executablePath': exe_path,
                            'headless': False})
    page = await browser.newPage()
    await page.goto('https://www.taobao.com')
    await asyncio.sleep(10)


asyncio.get_event_loop().run_until_complete(main())
```

发现页面显示出现了问题，需要手动调用setViewport方法设置显示页面的长宽像素。设置如下：

### 　执行js程序

拖动滚轮。调用evaluate方法。

```python
import asyncio
from pyppeteer import launch

width, height = 1366, 768


async def main():
    exe_path = 'C:\\zhenxin\\chrome-win\\chrome.exe'
    browser = await launch({'executablePath': exe_path,
                            'headless': False})
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=')
    await asyncio.sleep(6)
    # evaluate可以返回js程序的返回值
    dimensions = await page.evaluate('window.scrollTo(0,document.body.scrollHeight)')
    await asyncio.sleep(6)
    print(dimensions)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())

```

### 节点交互

Pyppeteer 三种解析方式
Page.querySelector()      # 选择器
Page.querySelectorAll()
Page.xpath()                   # xpath  表达式

简写方式为：

```
import asyncio
from pyppeteer import launch


async def main():
    # headless参数设为False，则变成有头模式
    exe_path = 'C:\\zhenxin\\chrome-win\\chrome.exe'
    browser = await  launch(
        {'executablePath': exe_path,
         'headless': False}
    )

    page = await browser.newPage()
    # 设置页面视图大小
    await page.setViewport(viewport={'width': 1280, 'height': 800})

    await page.goto('https://www.baidu.com/')
    # 节点交互
    await page.type('#kw', '周杰伦', {'delay': 1000})
    await asyncio.sleep(3)
    await page.click('#su')
    await asyncio.sleep(3)
    # 使用选择器选中标签进行点击
    alist = await page.querySelectorAll('.s_tab_inner > a')
    a = alist[3]
    await a.click()
    await asyncio.sleep(3)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
```

### 案例: 网易的新闻标题

```python
import asyncio
from pyppeteer import launch
from lxml import etree


async def main():
    # headless参数设为False，则变成有头模式
    browser = await launch(
        {'executablePath': 'C:\\zhenxin\\chrome-win\\chrome.exe',
         'headless': False}
    )

    page1 = await browser.newPage()
    # 设置页面视图大小
    await page1.setViewport(viewport={'width': 1280, 'height': 800})
    # 是否启用js


    page2 = await browser.newPage()
    await page2.setViewport(viewport={'width': 1280, 'height': 800})
    await page2.goto('https://news.163.com/domestic/')
    await page2.evaluate('window.scrollTo(0,document.body.scrollHeight)')
    page_text1 = await page2.content()

    await browser.close()

    return {'wangyi': page_text1}


def parse(task):
    content_dic = task.result()

    wangyi = content_dic['wangyi']

    tree = etree.HTML(wangyi)
    div_list = tree.xpath('//div[@class="data_row news_article clearfix "]')
    print(len(div_list))
    for div in div_list:
        title = div.xpath('.//div[@class="news_title"]/h3/a/text()')[0]
        print('wangyi:', title)


tasks = []
task1 = asyncio.ensure_future(main())
task1.add_done_callback(parse)
tasks.append(task1)
asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))

```


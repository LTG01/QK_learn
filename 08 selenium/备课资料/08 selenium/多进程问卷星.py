"""
    使用进程池，同时启动 5个 问卷星任务，一起完成
"""
# encoding:utf-8
from selenium import webdriver
import time
import csv
import multiprocessing
import concurrent.futures


def parser1(drive):
    """解析当前也买你的数据并返回"""
    data = []
    # 直接获取网页元素
    elements = drive.find_elements_by_css_selector('.itm')
    # 提取每一个人的评论
    for element in elements:
        cnt = element.find_element_by_css_selector('.cnt')
        t = element.find_element_by_css_selector('.time')
        # 将评论添加到评论列表
        data.append([cnt.text, t.text])
    return data


def save_data(data, songid):
    """写入数据方法"""
    with open(songid + '.csv', mode='a', encoding='utf-8-sig', newline='') as f:
        write = csv.writer(f)
        for d in data:
            write.writerow(d)


def download_comment(songid):
    drive = webdriver.Chrome()
    url = f'https://music.163.com/#/song?id={songid}'
    drive.get(url)
    drive.switch_to.frame(0)

    for i in range(3):
        data = parser1(drive)
        save_data(data, songid)
        js = 'window.scrollBy(0, 8000)'
        drive.execute_script(js)
        drive.implicitly_wait(10)
        drive.find_element_by_css_selector('.znxt').click()
        time.sleep(1)
    drive.quit()


if __name__ == '__main__':

    songids = ['1413361760', '1395792904', '1416370444', '1404885266']
    process_pool = concurrent.futures.ProcessPoolExecutor(max_workers=3)

    for url, name in songids[:3]:
        # download(url, name)
        process_pool.submit(download_comment, url, name)
    process_pool.shutdown()

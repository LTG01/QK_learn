
'''
验证码图片只有一张，不会变，变动的只是缺口的位置
'''

from io import BytesIO
from selenium import webdriver
import re
import requests
import random
from PIL import Image

url='http://www.cnbaowen.net/api/geetest/'

driver = webdriver.Chrome()

driver.get(url=url)
#等待页面加载完成
driver.implicitly_wait(20)

divlist1=driver.find_elements_by_css_selector('.gt_cut_bg.gt_show div')
divlist2=driver.find_elements_by_css_selector('.gt_cut_fullbg.gt_show div')
hover = driver.find_element_by_css_selector('.gt_slider_knob')
print(len(divlist1),divlist1)

def get_distance(image1, image2):
    """
    拿到滑动验证码需要移动的距离
    :param image1:没有缺口的图片对象
    :param image2:带缺口的图片对象
    :return:需要移动的距离
    """
    # print('size', image1.size)
    # rgb的差值不超过这一个范围 误差范围
    threshold = 50
    for i in range(0, image1.size[0]):  # 260
        for j in range(0, image1.size[1]):  # 160
            pixel1 = image1.getpixel((i, j))
            pixel2 = image2.getpixel((i, j))
            res_R = abs(pixel1[0] - pixel2[0])  # 计算RGB差
            res_G = abs(pixel1[1] - pixel2[1])  # 计算RGB差
            res_B = abs(pixel1[2] - pixel2[2])  # 计算RGB差
            if res_R > threshold and res_G > threshold and res_B > threshold:
                return i  # 需要移动的距离



def get_track(distance):
    """
    拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
    匀变速运动基本公式：
    ① v=v0+at
    ② s=v0t+(1/2)at²
    ③ v²-v0²=2as

    :param distance: 需要移动的距离
    :return: 存放每0.2秒移动的距离
    """
    print("distance", distance)
    # 初速度
    v = 0
    # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
    t = 2
    # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
    tracks = []
    # 当前的位移
    current = 0
    # 到达 mid 值开始减速(中点)
    mid = distance * 7 / 8
    # 多划出去 10 像素
    distance += 10  # 先滑过一点，最后再反着滑动回来
    # a = random.randint(1,3)
    while current < distance:
        # 设置速度
        if current < mid:
            # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
            a = random.randint(2, 4)  # 加速运动
        else:
            a = -random.randint(3, 5)  # 减速运动

        # 初速度
        v0 = v
        # 0.2 秒时间内的位移
        s = v0 * t + 0.5 * a * (t ** 2)
        # 当前的位置
        current += s
        # 添加到轨迹列表
        tracks.append(round(s))

        # 速度已经达到v,该速度作为下次的初速度
        v = v0 + a * t

    print(tracks)
    total = sum(tracks)
    # 对超出的移动的内容进行修正
    while (total - distance) > -13:
        # 反着滑动到大概准确位置
        tracks.append(-random.randint(2, 3))
        total = sum(tracks)

    print('tracks', tracks)
    print('sumtracks', sum(tracks))
    return tracks


def get_imgAndPos(divList,i=1):

    pos_list=[]
    img_url=''
    '''
    style="background-image: url("http://static.geetest.com/pictures/gt/579066de6/579066de6.webp"); background-position: -157px -58px;"
    '''
    for div in divList:
        mode='background-image: url\("(.*?)"\); background-position: (.*?)px (.*?)px;'
        print(div.get_attribute('style'))

        data =re.findall(mode,div.get_attribute('style'))
        pos={}
        pos['x']= int(data[0][1])
        pos['y'] = int(data[0][2])
        img_url = data[0][0]
        pos_list.append(pos)

    image_url = img_url.replace('webp', 'jpg')

    image_result = requests.get(image_url).content
    # 保存图片数据
    with open('{}.jpg'.format(i),'wb') as f:
        f.write(image_result)
    # 是一张无序的图片
    # 是一张无序的图片
    image_file = BytesIO(image_result)
    return image_file,pos_list

def create_img(image_file,pos_list,i=1):

    img= Image.open(image_file)

    new_img= Image.new('RGB',(260,116))
    up_list=[]
    down_list=[]
    for pos in pos_list:

        if pos['y']==-58:
            i = img.crop(abs(pos['x']),58,abs(pos['x']+10),116)
            up_list.append(i)

        if pos['y']==0:
            i = img.crop(abs(pos['x']),0,abs(pos['x']+10,58))
            down_list.append(i)

    off_set=0
    for im in up_list:
        new_img.paste(im,(off_set,0))
        off_set+=im.size[0]

    off_set=0
    for im in down_list:
        new_img.paste(im,(off_set,58))
        off_set+=im.size[0]

    new_img.save('{}.jpg'.format(i))
    return new_img

image_file1,pos_list1 =get_imgAndPos(divlist1)


image_file2,pos_list2 =get_imgAndPos(divlist2)

image1= create_img(image_file1,pos_list1,11)
image2=create_img(image_file2,pos_list2,22)

# 3. 求出需要移动的距离
distance = get_distance(image1, image2)
print(distance)
# 4. 构建移动轨迹
tracks = get_track(distance)
print(tracks)
"""滑动动作链"""
# 使用动作链进行滑动验证
action = webdriver.ActionChains(driver)
# 点击, 并且不释放
action.click_and_hold(hover).perform()

for track in tracks:
    # 操作本身就会有延时
    # 只要动作不像机器就没事
    action.move_by_offset(track, 0)
# 释放
action.release().perform()
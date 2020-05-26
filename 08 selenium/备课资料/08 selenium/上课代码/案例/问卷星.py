from selenium import webdriver
import random

drive = webdriver.Chrome(executable_path='../chromedriver.exe')

url = 'https://www.wjx.cn/jq/53732451.aspx'
drive.get(url)

click_div = [0, 1, 3, 4, 5, 7, 9]
check_div = [2, 8, 10, 11, 13]
order_div = [6]
score_div = [12]
answer_div = [14]

# 每一个题目的元素
elements = drive.find_elements_by_css_selector('.div_question')
print(len(elements))
print(elements)
# 第一道题目
for c in click_div:
    answer1 = elements[c]
    lis = answer1.find_elements_by_css_selector('li')
    # 随机填
    lis[random.randint(0, len(lis) - 1)].click()
    print(lis)

for c in check_div:
    # 第三题 多选题
    answer3 = elements[c]
    lis = answer3.find_elements_by_css_selector('li')
    # 随机选一半
    length = len(lis)
    l = [i for i in range(length)]
    print(l)
    l = random.choices(l, k=int(length / 2))
    for i in l:
        lis[i].click()

# 排序题
answer3 = elements[order_div[0]]
lis = answer3.find_elements_by_css_selector('li')
# 随机选一半
length = len(lis)
l = [i for i in range(length)]
# 排序进行点击
random.shuffle(l)
print(l)
for i in l:
    lis[i].click()

input()
drive.quit()

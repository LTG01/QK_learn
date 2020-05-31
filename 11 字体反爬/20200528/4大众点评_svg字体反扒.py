#--coding:utf-8--

import requests

from copyheaders import headers_raw_to_dict

import parsel
import re
import pprint

url='http://www.dianping.com/shop/130096343/review_all'

headers = '''
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
Cookie: _lxsdk_cuid=1725e53898cc8-00a56221c9380d-1b386257-13c680-1725e53898dc8; _lxsdk=1725e53898cc8-00a56221c9380d-1b386257-13c680-1725e53898dc8; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1590720433; _hc.v=ccc1d798-4f6d-50c4-d97b-3014a6707c85.1590720433; lgtoken=03b3f6a74-b893-46ba-a633-151609c7f68b; dplet=44ebdbaf1374446b79f584f3b3e0a3ea; dper=89f7587fe06f9b5a8127a798f3054d4e53e310e3d97392ae9d1cb4e6ec9fd2220296ffb08024e52137c90d24797d02b200ac2e1a2bc4c2fcbb7ae65522d6c966f01a276961001386332b0d9e0c0e25983b3d8e9692d22dde7b66f6f44932ccb1; ll=7fd06e815b796be3df069dec7836c3df; ua=%E9%80%86%E6%B5%81%E8%80%8C%E4%B8%8A_2962; ctu=fe900529419a03962c38d2c1153046d0867bdba9b652361c8b54a18a3abc6755; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1590720570; _lxsdk_s=1725e53898d-b38-ab0-c11%7C%7C41
'''


headers = headers_raw_to_dict(bytes(headers, encoding="utf-8"))
html_response = requests.get(url=url,headers=headers).text

# print(html_response)

with  open('dazhong.html','w') as f:

    f.write(html_response)

selector = parsel.Selector(html_response)
#
# total_reviews = selector.css('.reviews::text').get()
# print(total_reviews)
# total_price = selector.css('.price::text').get()
# print(total_price)
# total_score = selector.css('.rank-info .score .item::text').getall()
# print(total_score)
# adress = selector.css('.address-info::text').get()
# print(adress)

#获取页面反扒的位置

cc = selector.css('.phone-info cc::attr(class)').getall()

print(cc)



#获取css 文件路径
#    <link rel="stylesheet" type="text/css" href="//s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/534bd1e1c2f9db95b1372081831d10e1.css">

css_url = "http:"+re.findall('<link rel="stylesheet" type="text/css" href="(//s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/.*?\.css)">',html_response)[0]

print(css_url)


#获取 css内容

css_content = requests.get(css_url).text

print(css_content)




#获取类名称
'''
svgmtsi[class^="dm"]{width: 14px;height: 24px;margin-top: -14px;background-image:

cc[class^="tz"]{width: 14px;height: 16px;margin-top: -7px;

bb[class^="rt"]{width: 14px;height: 22px;margin-top: -1px;'''

background_images= re.findall('(\w+)\[class\^="(\w+)"\]\{width:.*?background-image: url\((.*?)\);',css_content)
print(background_images)


pattern = re.compile('.(\w+){background:-(\d+\.\d+)px -(\d+\.\d+)px;}')

class_map = re.findall(pattern, css_content)
print(class_map)

backgrounds_dic={}

for background_image in background_images:
    background_dic = {}
    back_type = background_image[0]
    back_className = background_image[1]
    back_url = 'http:'+background_image[2]

    # background_dic['type']=back_type
    background_dic['url'] = back_url
    class_name={}
    for item in class_map:
        if item[0].startswith(back_className):
            class_name[item[0]] =(float(item[1]),float(item[2]))
        pass

    background_dic[back_className]=class_name

    backgrounds_dic[back_type]=background_dic

pprint.pprint(backgrounds_dic)


# def download(name,url):
#     res = requests.get(url).content
#     with open(name,'wb') as f:
#         f.write(res)
#
# for items in background_image_classnames:
#
#     name = items[0]+'_'+items[1]+'.html'
#     url ="http:"+items[2]
#
#     download(name,url)


cc_url=backgrounds_dic.get('cc',{}).get('url',None)

# cc_url= 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/0459b8acc4f8ab52744631cbdbd26ef4.svg'
#
res = requests.get(cc_url).text

# res=''
# with  open('cc_tz.html','r') as f:
#
#     res=f.read()


#
xlist = re.findall('<text x="(.*?)".*?>(.*?)</text>',res)[0]
print(xlist)
xs = xlist[0].strip().split(' ')
print(len(xs),xs)
xindex=[int(i) for i in xs]

print(len(xindex),xindex)
value = list(xlist[1])

print(len(value),value)















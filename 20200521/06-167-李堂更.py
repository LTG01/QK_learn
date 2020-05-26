
import requests
import pprint
import json

url ='https://index.mysteel.com/newprice/getChartMultiCity.ms?callback=callback'


data ={

'catalog': '%E8%9E%BA%E7%BA%B9%E9%92%A2_:_%E8%9E%BA%E7%BA%B9%E9%92%A2',
'city': '%E4%B8%8A%E6%B5%B7,%E5%8C%97%E4%BA%AC,%E5%B9%BF%E5%B7%9E',
'spec': 'HRB400%2020MM_:_HRB400_20MM',
'startTime': '2019-05-21',
'endTime': '2020-05-21'
}
headers={

'Referer': 'https://index.mysteel.com/price/indexPrice.html',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',


}

res = requests.post(url=url,data=data,headers=headers).text

k= len(res)
data =res[9:k-2]
result = json.loads(data)
print(type(result),result)

shanghai= result['data'][0]['dateValueMap']

beijing= result['data'][1]['dateValueMap']
guangzhou= result['data'][2]['dateValueMap']

for item in result['data']:

    name =item['lineName']
    dateValueMap=item['dateValueMap']
    print('*'*100)
    for dateValue in dateValueMap:
        date = dateValue['date']
        value = dateValue['value']
        print(name,date,value)

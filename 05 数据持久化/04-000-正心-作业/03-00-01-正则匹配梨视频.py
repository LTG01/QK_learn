"""
    使用python请求此页面：https://www.pearvideo.com/video_1639869 将在获取的文本中会有下面这段内容

    var contId="1639869",liveStatusUrl="liveStatus.jsp",liveSta="",playSta="1",autoPlay=!1,isLiving=!1,isVrVideo=!1,hdflvUrl="",sdflvUrl="",hdUrl="",sdUrl="",ldUrl="",srcUrl="https://video.pearvideo.com/mp4/adshort/20200107/cont-1639869-14773063_adpkg-ad_hd.mp4",vdoUrl=srcUrl,skinRes="//www.pearvideo.com/domain/skin",videoCDN="//video.pearvideo.com";
var player;

    请将其中的视频连接提取出来，并将视频下载到本地。视频名为页面的标题
"""
import requests
import re
response = requests.get('https://www.pearvideo.com/video_1639869')
html = response.text
result = re.findall(',srcUrl="(.*?)"', html)
name = re.findall('<h1 class="video-tt">(.*?)</h1>', html)[0]
print(result)
print(name)
mp4_url = result[0]

response = requests.get(mp4_url)
with open(name+'.mp4', mode='wb') as f:
    f.write(response.content)

"""
    使用python请求此页面：https://www.pearvideo.com/video_1639869 将在获取的文本中会有下面这段内容

    var contId="1639869",liveStatusUrl="liveStatus.jsp",liveSta="",playSta="1",autoPlay=!1,isLiving=!1,isVrVideo=!1,hdflvUrl="",sdflvUrl="",hdUrl="",sdUrl="",ldUrl="",srcUrl="https://video.pearvideo.com/mp4/adshort/20200107/cont-1639869-14773063_adpkg-ad_hd.mp4",vdoUrl=srcUrl,skinRes="//www.pearvideo.com/domain/skin",videoCDN="//video.pearvideo.com";
var player;

    请将其中的视频连接提取出来，并将视频下载到本地。视频名为页面的标题
"""
import requests
import re
url = 'https://www.pearvideo.com/video_1639869'

res = requests.get(url=url).text
print(res)
murl = re.findall('srcUrl="(.*?)"',res,re.S)[0]
name = re.findall('<h1 class="video-tt">(.*?)</h1>',res,re.S)[0]


res= requests.get(murl).content
with open('{}.mp4'.format(name),'wb') as f:
    f.write(res)


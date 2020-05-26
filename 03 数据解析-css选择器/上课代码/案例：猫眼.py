import parsel

html = """

<!DOCTYPE html>

<!--[if IE 8]><html class="ie8"><![endif]-->
<!--[if IE 9]><html class="ie9"><![endif]-->
<!--[if gt IE 9]><!--><html><!--<![endif]-->
<head>
  <title>TOP100榜 - 猫眼电影 - 一网打尽好电影</title>
  
  <link rel="dns-prefetch" href="//p0.meituan.net"  />
  <link rel="dns-prefetch" href="//p1.meituan.net"  />
  <link rel="dns-prefetch" href="//ms0.meituan.net" />
  <link rel="dns-prefetch" href="//s0.meituan.net" />
  <link rel="dns-prefetch" href="//ms1.meituan.net" />
  <link rel="dns-prefetch" href="//analytics.meituan.com" />
  <link rel="dns-prefetch" href="//report.meituan.com" />
  <link rel="dns-prefetch" href="//frep.meituan.com" />

  
  <meta charset="utf-8">
  <meta name="keywords" content="猫眼电影,电影排行榜,热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100">
  <meta name="description" content="猫眼电影热门榜单,包括热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100,多维度为用户进行选片决策">
  <meta http-equiv="cleartype" content="yes" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="renderer" content="webkit" />

  <meta name="HandheldFriendly" content="true" />
  <meta name="format-detection" content="email=no" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="viewport" content="width=device-width, initial-scale=1">

  
  <script>"use strict";!function(){var i=0<arguments.length&&void 0!==arguments[0]?arguments[0]:"_Owl_",n=window;n[i]||(n[i]={isRunning:!1,isReady:!1,preTasks:[],dataSet:[],use:function(i,t){this.isReady&&n.Owl&&n.Owl[i](t),this.preTasks.push({api:i,data:[t]})},add:function(i){this.dataSet.push(i)},run:function(){var t=this;if(!this.isRunning){this.isRunning=!0;var i=n.onerror;n.onerror=function(){this.isReady||this.add({type:"jsError",data:arguments}),i&&i.apply(n,arguments)}.bind(this),(n.addEventListener||n.attachEvent)("error",function(i){t.isReady||t.add({type:"resError",data:[i]})},!0)}}},n[i].run())}();</script>
  <script>
  cid = "c_wx6zb55";
  ci = 70;
val = {"subnavId":4};    window.system = {};

  window.openPlatform = '';
  window.openPlatformSub = '';
  window.$mtsiFlag = '0';

  </script>
  <link rel="stylesheet" href="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/common.d1d257d3.css"/>
<link rel="stylesheet" href="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/board-index.92a06072.css"/>
  <script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/stat.88d57c80.js"></script>
  <script>if(window.devicePixelRatio >= 2) { document.write('<link rel="stylesheet" href="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image-2x.8ba7074d.css"/>') }</script>
  <style>
    @font-face {
      font-family: stonefont;
      src: url('//vfile.meituan.net/colorstone/fb9c55077ac8015c5035be1f94d34a6f3456.eot');
      src: url('//vfile.meituan.net/colorstone/fb9c55077ac8015c5035be1f94d34a6f3456.eot?#iefix') format('embedded-opentype'),
           url('//vfile.meituan.net/colorstone/6a4195f3fe38b2e176191731c24b3e7a2300.woff') format('woff');
    }

    .stonefont {
      font-family: stonefont;
    }
  </style>
  <script>
  var _hmt = _hmt || [];
  (function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?703e94591e87be68cc8da0da7cbd0be2";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
  })();
  </script>
</head>
<body>


<div class="header">
  <div class="header-inner">
          <a href="//maoyan.com" class="logo" data-act="icon-click"></a>
        <div class="city-container" data-val="{currentcityid:70 }">
            <div class="city-selected">
                <div class="city-name">
                  长沙
                  <span class="caret"></span>
                </div>
            </div>
            <div class="city-list" data-val="{ localcityid: 70 }">
                <div class="city-list-header">定位城市：<a class="js-geo-city" data-ci="70">长沙</a></div>
                
            </div>
        </div>


        <div class="nav">
            <ul class="navbar">
                <li><a href="/" data-act="home-click"  >首页</a></li>
                <li><a href="/films" data-act="movies-click" >电影</a></li>
                <li><a href="/cinemas" data-act="cinemas-click" >影院</a></li> 
                <li><a href="http://www.gewara.com">演出</a></li>
                
                <li><a href="/board" data-act="board-click"  class="active" >榜单</a></li>
                <li><a href="/news" data-act="hotNews-click" >热点</a></li>
                <li><a href="/edimall"  >商城</a></li>
            </ul>
        </div>

        <div class="user-info">
            <div class="user-avatar J-login">
              <img src="https://p0.meituan.net/movie/7dd82a16316ab32c8359debdb04396ef2897.png">
              <span class="caret"></span>
              <ul class="user-menu no-login-menu">
                <li><a href="javascript:void 0">登录</a></li>
              </ul>
            </div>
        </div>

        <form action="/query" target="_blank" class="search-form" data-actform="search-click">
            <input name="kw" class="search" type="search" maxlength="32" placeholder="找影视剧、影人、影院" autocomplete="off">
            <input class="submit" type="submit" value="">
        </form>

        <div class="app-download">
          <a href="/app" target="_blank">
            <span class="iphone-icon"></span>
            <span class="apptext">APP下载</span>
            <span class="caret"></span>
            <div class="download-icon">
                <p class="down-title">扫码下载APP</p>
                <p class='down-content'>选座更优惠</p>
            </div>
          </a>
        </div>
    
  </div>
</div>
<div class="header-placeholder"></div>

<div class="subnav">
  <ul class="navbar">
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:7}"
          href="/board/7"
      >热映口碑榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:6}"
          href="/board/6"
      >最受期待榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:1}"
          href="/board/1"
      >国内票房榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:2}"
          href="/board/2"
      >北美票房榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:4}"
          data-state-val="{subnavId:4}"
          class="active" href="javascript:void(0);"
      >TOP100榜</a>
    </li>
  </ul>
</div>


    <div class="container" id="app" class="page-board/index" >

<div class="content">
    <div class="wrapper">
        <div class="main">
            <p class="update-time">2020-05-16<span class="has-fresh-text">已更新</span></p>
            <p class="board-content">榜单规则：将猫眼电影库中的经典影片，按照评分和评分人数从高到低综合排序取前100名，每天上午10点更新。相关数据来源于“猫眼电影库”。</p>
            <dl class="board-wrapper">
                <dd>
                        <i class="board-index board-index-1">1</i>
    <a href="/films/1375" title="活着" class="image-link" data-act="boarditem-click" data-val="{movieId:1375}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/4c41068ef7608c1d4fbfbe6016e589f7204391.jpg@160w_220h_1e_1c" alt="活着" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1375" title="活着" data-act="boarditem-click" data-val="{movieId:1375}">活着</a></p>
        <p class="star">
                主演：葛优,巩俐,牛犇
        </p>
<p class="releasetime">上映时间：1994-05-17(法国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-2">2</i>
    <a href="/films/4883" title="钢琴家" class="image-link" data-act="boarditem-click" data-val="{movieId:4883}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/bcbe59fc51580317adf94537a61a1a26142090.jpg@160w_220h_1e_1c" alt="钢琴家" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/4883" title="钢琴家" data-act="boarditem-click" data-val="{movieId:4883}">钢琴家</a></p>
        <p class="star">
                主演：艾德里安·布洛迪,艾米莉娅·福克斯,米哈乌·热布罗夫斯基
        </p>
<p class="releasetime">上映时间：2002-05-24(法国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-3">3</i>
    <a href="/films/3294" title="勇敢的心" class="image-link" data-act="boarditem-click" data-val="{movieId:3294}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/f8e9d5a90224746d15dfdbd53d4fae3d209420.jpg@160w_220h_1e_1c" alt="勇敢的心" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/3294" title="勇敢的心" data-act="boarditem-click" data-val="{movieId:3294}">勇敢的心</a></p>
        <p class="star">
                主演：梅尔·吉布森,苏菲·玛索,帕特里克·麦高汉
        </p>
<p class="releasetime">上映时间：1995-05-18(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-4">4</i>
    <a href="/films/11237" title="阿飞正传" class="image-link" data-act="boarditem-click" data-val="{movieId:11237}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/85215b28d568ea8e2c97766edd95f890210522.jpg@160w_220h_1e_1c" alt="阿飞正传" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/11237" title="阿飞正传" data-act="boarditem-click" data-val="{movieId:11237}">阿飞正传</a></p>
        <p class="star">
                主演：张国荣,张曼玉,刘德华
        </p>
<p class="releasetime">上映时间：2018-06-25</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-5">5</i>
    <a href="/films/13824" title="射雕英雄传之东成西就" class="image-link" data-act="boarditem-click" data-val="{movieId:13824}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/86c5190ba1d1236093c13f2fe9ed8dd4150050.jpg@160w_220h_1e_1c" alt="射雕英雄传之东成西就" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/13824" title="射雕英雄传之东成西就" data-act="boarditem-click" data-val="{movieId:13824}">射雕英雄传之东成西就</a></p>
        <p class="star">
                主演：张国荣,梁朝伟,张学友
        </p>
<p class="releasetime">上映时间：1993-02-05(中国香港)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-6">6</i>
    <a href="/films/6796" title="爱·回家" class="image-link" data-act="boarditem-click" data-val="{movieId:6796}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/de1142a5dceb901eb939eb0bcfc2f88470909.jpg@160w_220h_1e_1c" alt="爱·回家" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/6796" title="爱·回家" data-act="boarditem-click" data-val="{movieId:6796}">爱·回家</a></p>
        <p class="star">
                主演：俞承豪,金艺芬,童孝熙
        </p>
<p class="releasetime">上映时间：2002-04-05(韩国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-7">7</i>
    <a href="/films/263" title="初恋这件小事" class="image-link" data-act="boarditem-click" data-val="{movieId:263}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/05bc2f0ccf97aacfa64fcac4f237cf8082385.jpg@160w_220h_1e_1c" alt="初恋这件小事" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/263" title="初恋这件小事" data-act="boarditem-click" data-val="{movieId:263}">初恋这件小事</a></p>
        <p class="star">
                主演：马里奥·毛瑞尔,平采娜·乐维瑟派布恩,阿查拉那·阿瑞亚卫考
        </p>
<p class="releasetime">上映时间：2012-06-05</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-8">8</i>
    <a href="/films/267" title="泰坦尼克号" class="image-link" data-act="boarditem-click" data-val="{movieId:267}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/b607fba7513e7f15eab170aac1e1400d878112.jpg@160w_220h_1e_1c" alt="泰坦尼克号" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/267" title="泰坦尼克号" data-act="boarditem-click" data-val="{movieId:267}">泰坦尼克号</a></p>
        <p class="star">
                主演：莱昂纳多·迪卡普里奥,凯特·温丝莱特,比利·赞恩
        </p>
<p class="releasetime">上映时间：1998-04-03</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">4</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-9">9</i>
    <a href="/films/1346" title="迁徙的鸟" class="image-link" data-act="boarditem-click" data-val="{movieId:1346}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/a1634f4e49c8517ae0a3e4adcac6b0dc43994.jpg@160w_220h_1e_1c" alt="迁徙的鸟" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1346" title="迁徙的鸟" data-act="boarditem-click" data-val="{movieId:1346}">迁徙的鸟</a></p>
        <p class="star">
                主演：雅克·贝汉,Philippe Labro
        </p>
<p class="releasetime">上映时间：2001-12-12(法国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-10">10</i>
    <a href="/films/790" title="蝙蝠侠：黑暗骑士" class="image-link" data-act="boarditem-click" data-val="{movieId:790}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/09658109acfea0e248a63932337d8e6a4268980.jpg@160w_220h_1e_1c" alt="蝙蝠侠：黑暗骑士" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/790" title="蝙蝠侠：黑暗骑士" data-act="boarditem-click" data-val="{movieId:790}">蝙蝠侠：黑暗骑士</a></p>
        <p class="star">
                主演：克里斯蒂安·贝尔,希斯·莱杰,阿伦·伊克哈特
        </p>
<p class="releasetime">上映时间：2008-07-14(阿根廷)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">3</i></p>        
    </div>

      </div>
    </div>

                </dd>
            </dl>

        </div>
            <div class="pager-main">
                
  
  <ul class="list-pager">



  
      <li class="active">
    <a class="page_1"
      href="javascript:void(0);" style="cursor: default"
  >1</a>

</li>
  <li >
    <a class="page_2"
      href="?offset=10"
  >2</a>

</li>
  <li >
    <a class="page_3"
      href="?offset=20"
  >3</a>

</li>
  <li >
    <a class="page_4"
      href="?offset=30"
  >4</a>

</li>
  <li >
    <a class="page_5"
      href="?offset=40"
  >5</a>

</li>

    <li class="sep">...</li>
      <li >
    <a class="page_10"
      href="?offset=90"
  >10</a>

</li>

  

<li>  <a class="page_2"
      href="?offset=10"
  >下一页</a>
</li>
</ul>


            </div>
    </div>
</div>

    </div>

<div class="footer">
  <p class="friendly-links">
    关于猫眼 :
    <a href="http://ir.maoyan.com/s/index.php#pageScroll0" target="_blank">关于我们</a>
    <span></span>
    <a href="http://ir.maoyan.com/s/index.php#pageScroll1" target="_blank">管理团队</a>
    <span></span>
    <a href="http://ir.maoyan.com/s/index.php#pageScroll2" target="_blank">投资者关系</a>
    &nbsp;&nbsp;&nbsp;&nbsp;
    友情链接 :
    <a href="http://www.meituan.com" data-query="utm_source=wwwmaoyan" target="_blank">美团网</a>
    <span></span>
    <a href="http://www.gewara.com" data-query="utm_source=wwwmaoyan">格瓦拉</a>
    <span></span>
    <a href="http://i.meituan.com/client" data-query="utm_source=wwwmaoyan" target="_blank">美团下载</a>
    <span></span>
    <a href="https://www.huanxi.com" data-query="utm_source=maoyan_pc" target="_blank">欢喜首映</a>
  </p>
  <p class="friendly-links">
    商务合作邮箱：v@maoyan.com
    客服电话：10105335
    违法和不良信息举报电话：4006018900
  </p>
  <p class="friendly-links">
    用户投诉邮箱：tousujubao@meituan.com
    舞弊线索举报邮箱：wubijubao@maoyan.com
  </p>
  <p class="friendly-links  credentials">
    <a href="/about/licence/1" target="_blank">中华人民共和国增值电信业务经营许可证 京B2-20190350</a>
    <span></span>
    <a href="/about/licence/4" target="_blank">营业性演出许可证 京演（机构）（2019）4094号</a>
  </p>
  <p class="friendly-links  credentials">
    <a href="/about/licence/3" target="_blank">广播电视节目制作经营许可证 （京）字第08478号</a>
    <span></span>
    <a href="/about/licence/2" target="_blank">网络文化经营许可证 京网文（2019）3837-369号 </a>
  </p>
  <p class="friendly-links  credentials">
    <a href="/rules/agreement" target="_blank">猫眼用户服务协议 </a>
    <span></span>
    <a href="/rules/rule" target="_blank">猫眼平台交易规则总则 </a>
    <span></span>
    <a href="/rules/privacy" target="_blank">隐私政策 </a>
    <span></span>
    <a href="https://www.12377.cn" target="_blank">网上有害信息举报专区 </a>
  </p>
  <p class="friendly-links  credentials">
    <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010102003232" target="_blank">京公网安备
      11010102003232号</a>
    <span></span>
    <a href="http://www.beian.miit.gov.cn/" target="_blank">京ICP备16022489号</a>
  </p>
  <p>北京猫眼文化传媒有限公司</p>
  <p>
    &copy;<span class="my-footer-year">2016</span>
    猫眼电影 maoyan.com</p>
  <div class="certificate">
    <a href="http://sq.ccm.gov.cn:80/ccnt/sczr/service/business/emark/toDetail/350CF8BCA8416C4FE0530140A8C0957E"
      target="_blank">
      <img src="http://p0.meituan.net/moviemachine/e54374ccf134d1f7b2c5b075a74fca525326.png" />
    </a>
    <a href="/about/licence/5" target="_blank">
      <img src="http://p1.meituan.net/moviemachine/805f605d5cf1b1a02a4e3a5e29df003b8376.png" />
    </a>
  </div>
</div>

    <script crossorigin="anonymous" src="//www.dpfile.com/app/owl/static/owl_1.7.11.js"></script>
    <script>
      Owl.start({
        project: 'com.sankuai.movie.fe.mywww',
        pageUrl: location.href.split('?')[0].replace(/\/\d+/g, '/:id'),
        devMode: false
      })
    </script>
    <script src="//s0.meituan.net/bs/?f=myfe/canary:mojo-0.1.2.js"></script>
    <script>
      MAInit({
        appkey: 'com.sankuai.movie.fe.mywww',
        app_name: 'maoyan-pc-web',
        app_version: '1.0.0',
      })
    </script>
    <!--[if IE 8]><script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/es5-shim.bbad933f.js"></script><![endif]-->
    <!--[if IE 8]><script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/es5-sham.d6ea26f4.js"></script><![endif]-->
    <script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/common.c4fcde76.js"></script>
<script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/board-index.e144d497.js"></script>
</body>
</html>
"""
selector = parsel.Selector(html)
span = selector.css('p.star:nth-child(2)').getall()
print(span)
# cla = selector.css('.star').getall()
# print(cla)
# cla = selector.css('.releasetime').getall()
# print(cla)

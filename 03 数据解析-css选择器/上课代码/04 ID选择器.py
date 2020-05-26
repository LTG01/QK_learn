import parsel

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标签选择器</title>
</head>
<style>
    p{
        color: #f00;
        font-size: 16px;
    }
</style>
<body>
<p id="content">css标签选择器的介绍</p>
<p class='tow'>标签选择器、类选择器、ID选择器</p>
<a href="https://www.baidu.com">百度一下</a>
<span> 我是一个span标签</span>
</body>
</html>
"""
# id 唯一的
# #
selector = parsel.Selector(html)
p = selector.css('#content').getall()
print(p)
p = selector.css('.tow').getall()
print(p)
p = selector.css('p').getall()
print(p)
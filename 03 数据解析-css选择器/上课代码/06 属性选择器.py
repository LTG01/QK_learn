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
<p id="content">css标签选择器的介绍</p>
<p class='tow'>标签选择器、类选择器、ID选择器</p>
<p class='tow'>标签选择器、类选择器、ID选择器</p>
<a href="https://www.baidu.com">百度一下</a>
<span> 我是一个span标签</span>
</body>
</html>
"""
# 组合选择器（多个选择器组合一起使用）
selector = parsel.Selector(html)
# 属性选择器 ::
# 如果需要文字属性 ::text
p = selector.css('p').getall()
print(p)
p = selector.css('p::text').getall()
print(p)
# 提取属性 ::attr(属性名)
a = selector.css('a::attr(href)').getall()
print(a)
p_class = selector.css('p::attr(class)').getall()
print(p_class)
p_class = selector.css('p::attr(id)').getall()
print(p_class)
# 笔记、不懂就查，有一个印象，当不懂知道去哪里找

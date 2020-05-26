import parsel
# 导入 parsel 库

# 字符串
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
<p>css标签选择器的介绍</p>
<p>标签选择器、类选择器、ID选择器</p>
<a href="https://www.baidu.com">百度一下</a>
<span> 我是一个span标签</span>
</body>
</html>
"""
# 把 html 字符串编程 parsel.Selector
# parsel.Selector 可以使用 css、xpath、re
selector = parsel.Selector(html)
print(selector)
print(dir(selector))
# 标签选择器，直接给标签的名字
# 直接提取是一个对象, getall 把对象编程字符串
span = selector.css('span').getall()
print(span)
p = selector.css('p').getall()
print(p)
body = selector.css('body').getall()
print(body)
# 现在只定位标签

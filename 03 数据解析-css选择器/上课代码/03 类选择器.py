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
<p>css标签选择器的介绍</p>
<p class='tow'>标签选择器、类选择器、ID选择器</p>
<a href="https://www.baidu.com">百度一下</a>
<span> 我是一个span标签</span>
</body>
</html>
"""

# class 才是类 才能使用类选择器
# href 标签里面的属性：属性提取器
# 类选择器，相同的类属性全部提取
# . 代表提取类型
selector = parsel.Selector(html)
p = selector.css('p').getall()
print(p)

p2 = selector.css('.tow').getall()
print(p2)

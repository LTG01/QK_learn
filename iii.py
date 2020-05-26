import time

localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

print (int(time.strftime("%m", time.localtime())))


# import pyecharts.options as opts
# from pyecharts.charts import Line
# from pyecharts.faker import Faker
#
# y = Faker.values()
# y[3], y[5] = None, None
# c = (
#     Line()
#     .add_xaxis(Faker.choose())
#     .add_yaxis("商家A", y, is_connect_nones=True)
#     .set_global_opts(title_opts=opts.TitleOpts(title="Line-连接空数据"))
#     .render("./kkk/line_connect_null.html")
# )



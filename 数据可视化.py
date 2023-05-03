from pyecharts import options as opts
from pyecharts.charts import Bar

import 数据分析


# 生成前num销量的产品
def popular_generate(num):
    popular_items = 数据分析.popular_items(10)
    print(type(popular_items))
    c = (
        Bar()
        .add_xaxis(popular_items['article'].tolist())  # 传入数据需为list
        .add_yaxis("销量", popular_items['Quantity'].tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="销量前" + str(num) + "的商品"),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-25)),
        )
        .render("bar_toolbox.html")
    )


def hourly_sales_generate():
    hourly_sales = 数据分析.hour_sales()
    print(hourly_sales)
    # print(type(hourly_sales))


if __name__ == "__main__":
    hourly_sales_generate()
    # popular_generate(10)

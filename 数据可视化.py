from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

import 数据分析


def popular_generate():
    popular_items = 数据分析.popular_items(10)
    c = (
        Bar()
        .add_xaxis(popular_items['Quantity'])
        .add_yaxis("商家A",Faker.values())
        # .add_yaxis("商家B", Faker.values())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-显示 ToolBox"),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(is_show=False),
        )
        .render("bar_toolbox.html")
    )


if __name__ == "__main__":
    popular_generate()

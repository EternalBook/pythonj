import pandas as pd


def sales_import():
    data_csv = pd.read_csv(r'./Bakery sales.csv')
    print(type(data_csv['unit_price']))
    # data_csv["unit_price"] = data_csv["unit_price"].str.replace("€", "")
    # data_csv["unit_price"] = data_csv["unit_price"].str.replace(",", ".")
    # data_csv["unit_price"] = data_csv["unit_price"].str.replace(" ", "")
    # data_csv["unit_price"] = data_csv["unit_price"].str.replace(r'\D', '').astype(float) / 100
    data_csv["unit_price"] = data_csv["unit_price"].str.replace(r'\D', '', regex=True).astype(float) / 100
    data_csv["sales volume"] = data_csv["Quantity"] * data_csv['unit_price']
    return data_csv


# 统计前num销量的产品
def popular_items(num):
    # 统计每种物品的销售数量
    item_count = sales_import().groupby('article').count()['Quantity'].reset_index()
    item_count.sort_values(by='Quantity', ascending=False, inplace=True)
    hot_items = item_count.head(num)
    hot_items.index = [i + 1 for i in range(num)]  # 推导式 遍历1到num的行索引
    return hot_items


def hour_sales():
    time_sales = sales_import()
    # 使用lambda表达式将时间列转换为小时
    time_sales['time'] = time_sales['time'].apply(lambda x: int(x.split(':')[0]))
    # hourly_sales = time_sales.groupby('time')['article'].count()
    hourly_sales = time_sales.groupby(['time', 'article'])['Quantity'].count().reset_index()
    # print(hourly_sales)
    hourly_sales.to_csv(r'1.csv')
    return hourly_sales
    # time_sales = time_sales['time'].apply(lambda x: int(x.split(':')[0]))
    # time_sales = time_sales.groupby('time')["Quantity"].count
    # hourly_sales = time_sales.groupby(['time', 'article'])['Quantity'].count().reset_index()
    # hourly_sales.index=[7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    # return hourly_sales


if __name__ == "__main__":
    hour_sales()
    # print(sales_import())

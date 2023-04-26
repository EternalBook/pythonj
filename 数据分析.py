import pandas as pd


def sales_import():
    data_csv = pd.read_csv(r'./Bakery sales.csv')
    return data_csv


# 统计前num销量的产品
def popular_items(num):
    # 统计每种物品的销售数量
    item_count = sales_import().groupby('article').count()['Quantity'].reset_index()
    item_count.sort_values(by='Quantity', ascending=False, inplace=True)
    hot_items = item_count.head(num)
    hot_items.index = [i+1 for i in range(num)]  # 推导式 遍历1到num的行索引
    return hot_items


if __name__ == "__main__":
    print(popular_items(10))

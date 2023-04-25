import pandas as pd


def sales_import():
    data_csv = pd.read_csv(r'./Bakery sales.csv')
    return data_csv


if __name__ == "__main__":
    print(sales_import())

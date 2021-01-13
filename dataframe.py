import json
import pandas as pd
import matplotlib.pyplot as plt


def plot_data(stock, company_name):
    file_path = "./data/" + "daily" + ".json"
    with open(file_path, mode="r") as file:
        daily = json.load(fp=file)

    # BAR
    # data_frame = pd.DataFrame.from_dict(daily["Time Series (Daily)"], orient="index", dtype=float)
    # print(data_frame)
    # """
    #              1. open  2. high     3. low  4. close   5. volume
    # 2021-01-11   849.400   854.43   803.6222    811.19  58833211.0
    # 2021-01-08   856.000   884.49   838.3900    880.02  75055528.0
    # 2021-01-07   777.630   816.99   775.2000    816.04  51498948.0
    #
    # """
    #
    # title = stock + ": " + company_name + " Closing Price"
    # data_frame.plot(kind="bar", y="4. close", title=title)
    # plt.show()

    # BOXPLOT
    data_frame = pd.DataFrame.from_dict(daily["Time Series (Daily)"], dtype=float)
    print(data_frame)
    """
                 2021-01-11   2021-01-08  ...   2020-08-20   2020-08-19
    1. open    8.494000e+02       856.00  ...      1860.68      1865.00
    2. high    8.544300e+02       884.49  ...      2021.99      1911.00
    3. low     8.036222e+02       838.39  ...      1857.06      1841.21
    4. close   8.111900e+02       880.02  ...      2001.83      1878.53
    5. volume  5.883321e+07  75055528.00  ...  20611796.00  12205331.00
    """
    data_frame = data_frame.drop("5. volume")
    print(data_frame)

    title = stock + ": " + company_name
    data_frame.boxplot(fontsize=6, rot=90)
    plt.show()

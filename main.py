import numpy as np


def read():
    rs = np.array([])
    with open("stock_market_data-AAPL.csv") as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            x, date, low, high, close, ope = line.split(",")
            np.vstack((rs, [date, low, high, close, ope]))
    return rs


if __name__ == "__main__":
    rs = read()
    print("stock_market_data-AAPL.csv read")
    print(rs[:10])

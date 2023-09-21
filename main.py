import pandas as pd


N_MA = 20


def read():
    return pd.read_csv("stock_market_data-AAPL.csv")


def form_X_and_Y(rs):
    sample_rs = rs.head(100)
    close = sample_rs['Close']
    X, Y = [], []
    for i in range(len(close) - N_MA - 1):
        x = close.iloc[i:i + N_MA + 1]
        y = close.iloc[i + N_MA + 1]
        X.append(x)
        Y.append(y)
    return X, Y


if __name__ == "__main__":
    rs = read()
    print("stock_market_data-AAPL.csv read")
    print(rs.head())

    X, Y = form_X_and_Y(rs)
    print("X formed")
    print(X)
    print("Y formed")
    print(Y)


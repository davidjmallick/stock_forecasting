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


def calculate_Y_prime(X):
    Y_prime = []
    for x in X:
        y_prime = x.mean()
        Y_prime.append(y_prime)
    return Y_prime


def calculate_RMSE(Y_prime, Y):
    sum_sq_error = 0
    for i in range(len(Y_prime)):
        sum_sq_error += (Y[i] - Y_prime[i])**2
    mse = sum_sq_error / len(Y_prime)
    return mse**(1/2)


if __name__ == "__main__":
    rs = read()
    print("stock_market_data-AAPL.csv read")
    print(rs.head())

    X, Y = form_X_and_Y(rs)
    print("X formed")
    print(X)
    print("Y formed")
    print(Y)

    Y_prime = calculate_Y_prime(X)
    print("Y_prime:")
    print(Y_prime)

    RMSE = calculate_RMSE(Y_prime, Y)
    print("RMSE:")
    print(RMSE)


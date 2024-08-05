
# ToDo: Put print output into... dataframe?? Table
# ToDo: Debug iloc in main.py??


import pandas as pd



def read():
    return pd.read_csv("stock_market_data-AAPL.csv", parse_dates=["Date"])


"""
@input rs:
@input n_ma:
@return X, Y: Tuple of Lists of Series
    X: List of Series, where each Series is >1 element
    Y: List of Series, where each Series is 1 element
"""
def form_Xs_and_Ys(rs, n_ma):
    sample_rs = rs.head(100)
    close = sample_rs['Close']
    X, Y = [], []
    for i in range(len(close) - n_ma - 1):
        x = close.iloc[i:i + n_ma + 1]
        y = close.iloc[i + n_ma + 1]
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
    print("\n\n")

    n_mas = [10, 20, 30]
    XYs = {}
    for n_ma in n_mas:
        X, Y = form_Xs_and_Ys(rs, n_ma)
        XYs[n_ma] = (X, Y)
    print("X(%d) formed. Head:" % n_mas[0])
    print(XYs[n_mas[0]][0][:1])
    print("Y(%d) formed. Head:" % n_mas[0])
    print(XYs[n_mas[0]][1][:1])
    print("\n\n")

    XYs_1 = {}
    for n_ma in XYs.keys():
        Y_prime = calculate_Y_prime(XYs[n_ma][0])
        XYs_1[n_ma] = (XYs[n_ma][0], XYs[n_ma][1], Y_prime)
        print("Y_prime:")
        print(Y_prime[:10])
    print("\n\n")

    for k, v in XYs_1.items():
        Y_prime = v[2]
        Y = v[1]
        RMSE = calculate_RMSE(Y_prime, Y)
        print("RMSE:")
        print(RMSE)


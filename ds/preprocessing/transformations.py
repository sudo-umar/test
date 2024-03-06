from pandas import DataFrame


def square(df: DataFrame):
    df.iloc[:, -1] = df.iloc[:, -1].apply(lambda x: x ** 2)
    return df


def fib(n) -> int:
    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    return old


def rfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return rfib(n - 1) + rfib(n - 2)

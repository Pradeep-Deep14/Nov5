def func(arr: list):
    gen=(name for name in arr if len(arr)>=3)
    arr=["Peter","Mary"]
    return list(gen)

arr=["Joe","Peter","Paul"]

print(func(arr))
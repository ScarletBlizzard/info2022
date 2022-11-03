class YieldAverage(Exception):
    pass

class YieldVariance(Exception):
    pass

class YieldCount(Exception):
    pass


def data_coroutine():
    data = []
    try:
        while True:
            try:
                x = yield
                data.append(x)
            except YieldAverage:
                yield sum(data) / len(data)
            except YieldVariance:
                avg = sum(data) / len(data)
                yield sum((i-avg)**2 for i in data) / (len(data)-1)
            except YieldCount:
                yield len(data)
    finally:
        return


if __name__ == "__main__":
    coroutine = data_coroutine()
    next(coroutine)
    for i in map(float, input().split(",")):
        coroutine.send(i)

    print("Среднее:", coroutine.throw(YieldAverage))
    next(coroutine)
    print("Несмещённая дисперсия:", coroutine.throw(YieldVariance))
    next(coroutine)
    print("Кол-во элементов:", coroutine.throw(YieldCount))
    next(coroutine)
    coroutine.close()

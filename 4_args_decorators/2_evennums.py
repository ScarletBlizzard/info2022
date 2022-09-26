def decorator(func):

    def wrapper(numbers):
        count = func(numbers)
        if count == 0:
            print("Нет")
        elif count > 10:
            print("Очень много")

    return wrapper


@decorator
def count_even_nums(numbers):
    return len([x for x in numbers if int(x) % 2 == 0])


if __name__ == "__main__":
    count_even_nums(input().split())

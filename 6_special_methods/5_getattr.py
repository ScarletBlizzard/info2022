def none_attr(cls):
    def getattr(self, name):
        setattr(self, name, None)

    cls.__getattr__ = getattr
    return cls


@none_attr
class SomeClass(object):
    pass


if __name__ == "__main__":
    instance = SomeClass()
    instance.smth
    print(instance.__dict__)
    print(SomeClass().__dict__)

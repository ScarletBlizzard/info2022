class ForbiddenStringMetaclass(type):
    def __init__(cls, name, bases, attrs):
        FORBIDDEN_STRING = "stupid"
        for key, val in attrs.items():
            if callable(val) and FORBIDDEN_STRING in key:
                raise ValueError(("Class can't have method with name " + \
                    f"that contains string \"{FORBIDDEN_STRING}\""))
        super().__init__(name, bases, attrs)
        

class SomeClass(metaclass=ForbiddenStringMetaclass):
    stupid_attr = 0

    def stupid_function():
        pass

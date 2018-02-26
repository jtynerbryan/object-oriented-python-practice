# make a version of str that's always reversed
# remember str's are immutable
# when creating custom built-ins from an immutable datatype, use new() instead of __inti__()
# __new__ is used to create a new instance
# __init__ is used to initialize and instance that has already been created
class ReversedStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self

import copy

class FilledList(list):
    def __init__(self, count, value,  *args, **kwargs):
        super().__init__()

        for _ in range(count):
            self.append(copy.copy(value))

# __get_attribute__ lets you use . to look up key/values in dicts as you would with a js object
class JSObject(dict):
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            # this is calling dict's __get_attribute__() method
            return super().__getattribute__(item)

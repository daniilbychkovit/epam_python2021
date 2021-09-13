# I decided to write a code that generates data filtering object from a list of keyword parameters:

class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    """
    def __init__(self, *functions):
        self.functions = functions

    def apply(self, data):
        print(self.functions)
        return [item for item in data if all([i(item) for i in self.functions])]


positive_even = Filter(lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int))
print(positive_even.apply(range(100)))


def make_filter(**keywords):
    """
        Generate filter object for specified keywords
    """
    filter_funcs = ()
    for key, value in keywords.items():
        def keyword_filter_func(value):
            return value[key] == value
        filter_funcs += (keyword_filter_func,)
        print(filter_funcs)
        print(Filter(filter_funcs))
    return Filter(filter_funcs)



sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    }
]

print(make_filter(name='polly', type='bird').apply(sample_data))

# make_filter(name='polly', type='bird').apply(sample_data) should return only second entry from the list

# There are multiple bugs in this code. Find them all and write tests for faulty cases.

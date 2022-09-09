from twentyOneDigitsGenerator import twentyOneDigitsGenerator

def fakeGenerator(list):
    while True:
        for i in list:
            yield i


def test_twentyOne_1():
    generator = fakeGenerator([1,2,3,4,5,6,7,8,9])
    x = twentyOneDigitsGenerator(generator).__next__()
    assert x == 123456789123456789123

def test_twentyOne_2():
    generator = fakeGenerator([1])
    x = twentyOneDigitsGenerator(generator).__next__()
    assert x == 111111111111111111111
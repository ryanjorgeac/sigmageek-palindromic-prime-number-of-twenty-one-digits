from anyNumberOfDigitsGenerator import anyNumberOfDigitsGenerator

def fakeGenerator(list):
    while True:
        for i in list:
            yield i


def test_4_digits_generator():
    generator = fakeGenerator([1,2,3,4,5,6,7,8,9])
    x = anyNumberOfDigitsGenerator(generator, 4).__next__()
    assert x == 1234

def test_10_digits_generator():
    generator = fakeGenerator([1])
    x = anyNumberOfDigitsGenerator(generator, 10).__next__()
    assert x == 1111111111

def test_50_digits_generator():
    generator = fakeGenerator([1,4,7,0,2])
    x = anyNumberOfDigitsGenerator(generator, 50).__next__()
    assert x == 14702147021470214702147021470214702147021470214702
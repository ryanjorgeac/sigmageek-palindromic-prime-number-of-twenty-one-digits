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

def test_number_with_zero_on_the_road():
    generator = fakeGenerator([1, 0, 2, 3, 4, 5])
    listNumbers = []
    x = anyNumberOfDigitsGenerator(generator, 2)
    z = x.__next__()
    y = x.__next__()
    assert z == 10 and y == 2

def test_number_starting_with_zero():
    generator = fakeGenerator([0, 1, 2, 3, 4, 5])
    listNumbers = []
    x = anyNumberOfDigitsGenerator(generator, 2)
    z = x.__next__()
    assert z == 12

def test_number_starting_with_two_zeros():
    generator = fakeGenerator([0, 0, 2, 3, 4, 5])
    x = anyNumberOfDigitsGenerator(generator, 2)
    z = x.__next__()
    assert z == 2

def test_number_starting_with_three_zeros():
    generator = fakeGenerator([0, 0, 0, 3, 4, 5])
    x = anyNumberOfDigitsGenerator(generator, 2)
    z = x.__next__()
    assert z == 0

if __name__ == "__main__":
    test_number_starting_with_two_zeros()

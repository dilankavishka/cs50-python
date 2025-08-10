from calculator import square

def main():
    test_square()

#def test_square():
    #if square(2) != 4:
    #    raise Exception("Test failed: square(2) should be 4")
    #if square(3) != 9:
    #    raise Exception("Test failed: square(3) should be 9")
    #if square(4) != 16:
    #    raise Exception("Test failed: square(4) should be 16")

    #try:
    #    assert square(2) == 4
    #except AssertionError:
    #    print("Test failed: square(2) should be 4")
    #try:
    #    assert square(3) == 9
    #except AssertionError:
    #    print("Test failed: square(3) should be 9")
    #try:
    #    assert square(4) == 16
    #except AssertionError:
    #    print("Test failed: square(4) should be 16")
    #try:
    #    assert square(0) == 0
    #except AssertionError:
    #    print("Test failed: square(0) should be 0")

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16

def test_zero():
    assert square(0) == 0

if __name__ == "__main__":
    main()
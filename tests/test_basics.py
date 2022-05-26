import os 
import testbook
path = os.getcwd()
_path = "{}/basics.ipynb".format(path)

@testbook.testbook(_path, execute=True)
def test_sum_list(tb):
    func = tb.ref("sum_list")
    assert func([1,1,2,3,2]) == 9

@testbook.testbook(_path, execute=True)
def test_product_or_sum(tb):
    func2 = tb.ref("product_or_sum")
    assert func2(2,3) == 6
    assert func2(40,50) == 90
    
@testbook.testbook(_path, execute=True)
def test_check_palindrome(tb):
    func3 = tb.ref("check_palindrome")
    assert func3(222) == True
    assert func3(4050) == False

@testbook.testbook(_path, execute=True)
def test_first_mid_then_last(tb):
    func4 = tb.ref("first_mid_then_last")
    assert func4("Peter") == "Ptr"
    assert func4("Wednesday") == "Wey"

@testbook.testbook(_path, execute=True)
def test_mult_table(tb):
    func5 = tb.ref("mult_table")
    assert func5(2) == [2,4,6,8,10,12,14,16,18,20]

@testbook.testbook(_path, execute=True)
def test_largest(tb):
    func6 = tb.ref("largest")
    x = [2,4,6,8,10,12,14,16,18,20]
    assert func6(x) == 20
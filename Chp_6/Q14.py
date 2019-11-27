import sys


def is_even(n):
    e = n % 2
    if e == 0:
        return True
    if e != 0:
        return False


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(is_even(10) == True)
    test(is_even(167) == False)
    test(is_even(24568) == True)


test_suite()

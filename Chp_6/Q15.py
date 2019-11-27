# a)

import sys


def is_odd(n):
    e = n % 2
    if e == 0:
        return False
    if e != 0:
        return True


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
    test(is_odd(10) == False)
    test(is_odd(167) == True)
    test(is_odd(24568) == False)


test_suite()

# b)

import sys


def is_even(n):
    e = n % 2
    if e == 0:
        return True
    if e != 0:
        return False


def is_odd(n):
    if is_even(n) == True:
        return False
    if is_even(n) == False:
        return True


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
    test(is_odd(10) == False)
    test(is_odd(167) == True)
    test(is_odd(24568) == False)


test_suite()

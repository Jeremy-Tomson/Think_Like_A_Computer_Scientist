# Q6

import sys


def days_in_month(x):
    if x == "January":
        return 31
    if x == "February":
        return 28
    if x == "March":
        return 31
    if x == "April":
        return 30
    if x == "May":
        return 31
    if x == "June":
        return 30
    if x == "July":
        return 31
    if x == "August":
        return 31
    if x == "September":
        return 30
    if x == "October":
        return 31
    if x == "November":
        return 30
    if x == "December":
        return 31


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
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)


test_suite()

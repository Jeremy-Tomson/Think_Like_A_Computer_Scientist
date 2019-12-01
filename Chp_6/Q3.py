# Q3

import sys


def day_name(x):
    if x == 0:
        return "Sunday"
    if x == 1:
        return "Monday"
    if x == 2:
        return "Tuesday"
    if x == 3:
        return "Wednesday"
    if x == 4:
        return "Thursday"
    if x == 5:
        return "Friday"
    if x == 6:
        return "Saturday"


def day_num(x):
    if x == "Sunday":
        return 0
    if x == "Monday":
        return 1
    if x == "Tuesday":
        return 2
    if x == "Wednesday":
        return 3
    if x == "Thursday":
        return 4
    if x == "Friday":
        return 5
    if x == "Saturday":
        return 6


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
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)


test_suite()

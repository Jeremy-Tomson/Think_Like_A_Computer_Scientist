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
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)


test_suite()

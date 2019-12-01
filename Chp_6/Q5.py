# Q5

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


def day_add(today, stay):
    today = day_num(today)
    if (stay > -7):
        day_back = (stay % 7) + today
        result = day_name(day_back)
        return result
    elif stay < -7:
        day_back = (stay % -7) + today
        result = day_name(day_back)
        return result
    else:
        day_back = (stay % 7) + today
        result = day_name(day_back)
        return result


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
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")


test_suite()

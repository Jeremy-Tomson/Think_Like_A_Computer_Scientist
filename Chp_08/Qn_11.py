# Q11

import sys


def count_substring(sub_string, string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count


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
    test(count_substring("is", "Mississippi") == 2)
    test(count_substring("an", "banana") == 2)
    test(count_substring("ana", "banana") == 2)
    test(count_substring("nana", "banana") == 1)
    test(count_substring("nanan", "banana") == 0)
    test(count_substring("aaa", "aaaaaa") == 4)


test_suite()

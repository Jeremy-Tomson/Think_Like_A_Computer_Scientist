# Q10

import sys


def reverse(string):
    string_length = len(string)
    return string[string_length::-1]


def is_palindrome(string):
    rev = reverse(string)

    if string == rev:
        return True
    else:
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
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(" "))  # An empty string is a palindrome!


test_suite()

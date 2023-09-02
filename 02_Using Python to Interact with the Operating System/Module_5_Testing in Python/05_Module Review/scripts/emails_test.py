#!/usr/bin/env python3

import unittest
from email import find_email


class Emailstest(unittest.TestCase):
    def test_basic(self):
        testcase = [None, "Bree", "Campbell"]
        expected = "breee@abc.edu"
        self.assertEqual(find_email(testcase), expected)

    def test_one_name(self):
        testcase = [None, "John"]
        excepted = "Missing parameters"
        self.assertEqual(find_email(testcase), excepted)

    def test_two_name(self):
        testcase = [None, "Roy","Cooper"]
        excepted = "No email address found"
        self.assertEqual(find_email(testcase), excepted)
         


if __name__ == "__main__":
    unittest.main()
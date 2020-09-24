"""Unit tester"""
import unittest
from dslib import *

# Globals: debug (WIP)
debug = False

class StatTypicalTest(unittest.TestCase):
    """Tests for stat_typical.py"""
    def test_find_median(self):
        """
        Test median: The median of [0,1,2,3,4,5] is 2.5.

        :return: stuff
        """
        test_arr = []
        for i in range(6):
            test_arr.append(i)
        self.assertEqual(stat_typical.find_median(test_arr), 2.5, "Error, med test fail")

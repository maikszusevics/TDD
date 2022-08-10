import pytest
import unittest
from calc import SimpleCals

class Caltests(unittest.TestCase):
    calc_obj = SimpleCals()

    def test_add(self):
        self.assertEqual(self.calc_obj.add(4,2),6)

    def test_sub(self):
        self.assertEqual(self.calc_obj.subtract(4,2),2)

    def test_mult(self):
        self.assertEqual(self.calc_obj.multiply(4,2),8)

    def test_div(self):
        self.assertEqual(self.calc_obj.divide(4,2),2)#

    def test_dob(self):
        self.assertEqual(self.calc_obj.DOBcalc(10,4),"10/4")

    def test_remain(self):
        self.assertEqual(self.calc_obj.remainders(11, 2), 1)

    def test_cmconvert(self):
        self.assertEqual(self.calc_obj.cmtom(10), 0.1)
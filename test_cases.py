#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


# テストケース
class TestCalc (unittest.TestCase):

    def test_sample1(self):
        self.assertEqual(21, calc(3, 7))

    def test_sample2(self):
        self.assertEqual(-1, calc(0, 150))

    def test_sample3(self):
        self.assertEqual(-1, calc('a', 'b'))

    def test_sample4(self):
        self.assertEqual(-1, calc(0.1, 999))

    def test_sample5(self):
        self.assertEqual(-1, calc(1, 999.1))

    def test_sample6(self):
        self.assertEqual(-1, calc('A', 999))

    def test_sample7(self):
        self.assertEqual(-1, calc(-1, 1))

    def test_sample8(self):
        self.assertEqual(-1, calc(0, 999))

    def test_sample9(self):
        self.assertEqual(998001, calc(999, 999))

    def test_sampleq10(self):
        self.assertEqual(-1, calc(500.5, 999))

    def test_sample11(self):
        self.assertEqual(751494, calc(998, 753))

    def test_sample12(self):
        self.assertEqual(250000, calc(500, 500))

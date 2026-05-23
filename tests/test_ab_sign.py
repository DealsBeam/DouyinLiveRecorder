import unittest
import sys
import os
sys.path.append(os.getcwd())
from src import ab_sign

class TestAbSign(unittest.TestCase):
    def test_ab_sign_format(self):
        res = ab_sign.ab_sign("test=1", "Mozilla/5.0")
        self.assertTrue(res.endswith("="))

import unittest
import sys
import os
sys.path.append(os.getcwd())
from src import utils

class TestUtils(unittest.TestCase):
    def test_remove_emojis(self):
        self.assertEqual(utils.remove_emojis("test 🚀 emoji"), "test  emoji")
        self.assertEqual(utils.remove_emojis("no emoji"), "test emoji".replace("test ", "no "))

# test_headlessui.py
"""
Tests for HeadlessUI module.
"""

import unittest
from headlessui import HeadlessUI

class TestHeadlessUI(unittest.TestCase):
    """Test cases for HeadlessUI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HeadlessUI()
        self.assertIsInstance(instance, HeadlessUI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HeadlessUI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

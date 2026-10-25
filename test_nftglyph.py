# test_nftglyph.py
"""
Tests for NftGlyph module.
"""

import unittest
from nftglyph import NftGlyph

class TestNftGlyph(unittest.TestCase):
    """Test cases for NftGlyph class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = NftGlyph()
        self.assertIsInstance(instance, NftGlyph)

    def test_run_method(self):
        """Test the run method."""
        instance = NftGlyph()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

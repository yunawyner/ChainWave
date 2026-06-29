# test_chainwave.py
"""
Tests for ChainWave module.
"""

import unittest
from chainwave import ChainWave

class TestChainWave(unittest.TestCase):
    """Test cases for ChainWave class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainWave()
        self.assertIsInstance(instance, ChainWave)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainWave()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

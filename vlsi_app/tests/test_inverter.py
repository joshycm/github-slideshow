import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from inverter import Inverter

class TestInverter(unittest.TestCase):
    """Test suite for the Inverter class."""

    def test_logic(self):
        """Test the logic of the inverter."""
        inv = Inverter()

        inv.connect(True)
        inv.logic()
        self.assertEqual(inv.output, False)

        inv.connect(False)
        inv.logic()
        self.assertEqual(inv.output, True)

    def test_unconnected_input(self):
        """Test that an error is raised for an unconnected input."""
        inv = Inverter()
        with self.assertRaises(ValueError):
            inv.logic()

if __name__ == '__main__':
    unittest.main()

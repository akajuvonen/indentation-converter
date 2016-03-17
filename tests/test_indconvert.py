import unittest
from indconvert import indentation_converter

class TestIndentationConverter(unittest.TestCase):
    """Tests for indentation parsing."""
    def test_indent_converter(self):
        """Test that indentation parsing works in a normal situation."""
        # Set the lines and expected result of conversion
        testlines = ['asd','  asd','    asd']
        expectedlines = ['asd','    asd','        asd']
        # Compare the results
        for tline,eline in zip(testlines,expectedlines):
            self.assertEqual(indentation_converter(tline),eline)

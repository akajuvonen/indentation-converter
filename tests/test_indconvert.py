import unittest
from indconvert import indentation_converter
from indconvert import IndentationException

class TestIndentationConverter(unittest.TestCase):
    """Tests for indentation parsing."""
    def test_indent_converter(self):
        """Test that indentation parsing works in a normal situation"""
        # Set the lines and expected result of conversion
        testlines = ['asd','  asd','    asd']
        expectedlines = ['asd','    asd','        asd']
        # Compare the results
        for tline,eline in zip(testlines,expectedlines):
            self.assertEqual(indentation_converter(tline),eline)

    def test_abnormal_indent_count(self):
        """Test that an exception is raised when ind count does not match the file"""
        testline = '   asd'
        self.assertRaises(IndentationException,indentation_converter,testline,' ',2,4)
        

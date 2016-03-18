import unittest
from indconvert import parse_args

class TestArgParse(unittest.TestCase):
    """Tests for argument parsing."""
    def test_arg_parse(self):
        """Test that argument parsing works normally."""
        args = ['-f','filename','-i',' ','-o','2','-n','4']
        fn,i,o,n = parse_args(args)
        self.assertEqual(fn,args[1])
        self.assertEqual(i,args[3])
        self.assertEqual(o,int(args[5]))
        self.assertEqual(n,int(args[7]))

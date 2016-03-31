import unittest
from indconvert import parse_args

# Note:
# There could (and should) be many other tests, such as tests for
# missing arguments, or invalid argument types. However, argparse
# shows a message and exits when anything goes wrong. It's not very
# test friendly. Perhaps these will be added later.

class TestArgParse(unittest.TestCase):
    """Tests for argument parsing."""
    def test_arg_parse(self):
        """Test that argument parsing works normally"""
        args = ['-f','filename','-i',' ','-o','2','-n','4']
        fn,i,o,n = parse_args(args)
        self.assertEqual(fn,args[1])
        self.assertEqual(i,args[3])
        self.assertEqual(o,int(args[5]))
        self.assertEqual(n,int(args[7]))

    def test_arg_missing(self):
        """Test missing argument"""
        # This will done later, since when an argument is missing
        # argparse just give sys.exit, which is problematic for
        # testing and gives an error.
        pass

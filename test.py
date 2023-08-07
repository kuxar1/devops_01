"""Import requirements"""
import unittest
import io
from unittest.mock import patch

# Import the function to test
from hello_world import print_hello

class TestHelloWorld(unittest.TestCase):
    """ Class for testing functiong"""
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_hello(self, mock_stdout):
        """Funcion what test output"""
        # Capture the output of the print statement
        print_hello()
        # Get the actual output
        actual_output = mock_stdout.getvalue()
        # Compare the actual output with the expected output
        expected_output = "Hello world!\n"
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()

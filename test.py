"""Import requirements"""
import unittest
from unittest.mock import patch
import io

# Create test class
class TestMain(unittest.TestCase):
    """Funcion what test output"""
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main(self, mock_stdout):
        """Funcion what test output"""
        import hello_world
        # Get the actual output
        actual_output = mock_stdout.getvalue()
        # Compare the actual output with the expected output
        expected_output = "Hello world!\n"  # Note: Include the newline character at the end
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
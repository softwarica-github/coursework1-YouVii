import unittest
from unittest.mock import Mock, patch
import server  # Import the server module to be tested

class TestServerFunctions(unittest.TestCase):

    def setUp(self):
        self.mock_client = Mock()
        self.username = "test_user"

    def test_listen_for_messages(self):
        # Mock the behavior of the client.recv method to return a string
        self.mock_client.recv.return_value.decode.return_value = "Test message"

        # Call listen_for_messages with the mock client
        with patch('builtins.print'):
            server.listen_for_messages(self.mock_client, self.username)

        # Implement assertions here to test the behavior of listen_for_messages
        # For example, you can assert that the send_messages_to_all function is called

    # Implement similar tests for other server functions

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch, MagicMock
import client

class TestClient(unittest.TestCase):

    @patch('client.socket')
    def test_connect_success(self, mock_socket):
        # Mock the socket and its behavior
        mock_socket.AF_INET = MagicMock()
        mock_socket.SOCK_STREAM = MagicMock()
        mock_client = MagicMock()
        mock_socket.socket.return_value = mock_client

        # Mock the input and return values for input function
        mock_input = MagicMock(side_effect=["Username", "Message"])
        client.input = mock_input

        # Call the connect function
        client.connect()

        # Assert that the appropriate methods were called on the mock objects
        mock_socket.socket.assert_called_once_with(mock_socket.AF_INET, mock_socket.SOCK_STREAM)
        mock_client.connect.assert_called_once_with((client.HOST, client.PORT))
        mock_client.sendall.assert_called_once()
        mock_input.assert_called()

if __name__ == '__main__':
    unittest.main()

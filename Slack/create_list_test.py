import unittest
from unittest.mock import patch
from colors import colors
from create_list import channel_list, user_list

class TestAPIFunctions(unittest.TestCase):

    @patch("builtins.print")
    def test_channel_list_success(self, mock_print):
        options = []
        response = {
            "ok": True,
            "channels": [
                {"id": "channel1", "name": "Channel 1"},
                {"id": "channel2", "name": "Channel 2"},
                {"id": "channel3", "name": "Channel 3"}
            ]
        }

        options = channel_list(options, response)

        expected_options = [
            "Channel 1 = channel1",
            "Channel 2 = channel2",
            "Channel 3 = channel3"
        ]

        self.assertEqual(options, expected_options)
        mock_print.assert_called_once_with("")


    def test_user_list(self):
        options = []
        response = {
            "ok": True,
            "members": [
                {"id": "user1", "name": "User 1"},
                {"id": "user2", "name": "User 2"},
                {"id": "user3", "name": "User 3"}
            ]
        }

        options = user_list(options, response)

        expected_options = [
            "User 1 = user1",
            "User 2 = user2",
            "User 3 = user3"
        ]

        self.assertEqual(options, expected_options)

if __name__ == '__main__':
    unittest.main()

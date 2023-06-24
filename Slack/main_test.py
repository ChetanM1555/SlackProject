import unittest
from unittest.mock import patch
from io import StringIO
from slack_sdk.web import WebClient
from simple_term_menu import TerminalMenu
from colors import colors
import create_list as c
import main

class TestScript(unittest.TestCase):


    @patch("builtins.input", side_effect=["slack_token", "2", "user_invite", "user1", "channel1", "3"])
    @patch("slack_sdk.web.WebClient.users_list")
    def test_user_invite_success(self, mock_users_list, mock_input):
        mock_users_list.return_value = {
            "ok": True,
            "members": [
                {"id": "user1", "name": "User 1"},
                {"id": "user2", "name": "User 2"},
                {"id": "user3", "name": "User 3"}
            ]
        }

        with patch("slack_sdk.web.WebClient.conversations_list") as mock_conversations_list:
            mock_conversations_list.return_value = {
                "ok": True,
                "channels": [
                    {"id": "channel1", "name": "Channel 1"},
                    {"id": "channel2", "name": "Channel 2"},
                    {"id": "channel3", "name": "Channel 3"}
                ]
            }

            with patch("slack_sdk.web.WebClient.conversations_invite") as mock_conversations_invite:
                mock_conversations_invite.return_value = {"ok": True}

                # Redirect stdout to capture print statements
                captured_output = StringIO()
                with patch("sys.stdout", captured_output):
                    main.main()

                # Retrieve the captured print output
                output = captured_output.getvalue()

                # Assert expected output
                expected_output = (
                    "Who would you like to invite?\n"
                    "Where do you want to invite this person?\n"
                )

                self.assertIn(expected_output, output)
if __name__ == '__main__':
    unittest.main()

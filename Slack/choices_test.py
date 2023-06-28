import unittest
from unittest.mock import MagicMock
import choices as h

class choices_test(unittest.TestCase):
    def test_choose_channel_option(self):
        options2 = ["Channel", "Invite Something", "Quit", "default"]
        colors = MagicMock()
        client = MagicMock()
        c = MagicMock()
        ans = 0
        options = MagicMock()

        mock_conversations_list = MagicMock()
        client.conversations_list = MagicMock(return_value=mock_conversations_list)

        mock_channel_list = MagicMock()
        c.channel_list = MagicMock(return_value=mock_channel_list)

        quit, response, response2, options = h.choose(options2, colors, client, c, ans, options)

        self.assertFalse(quit)
        self.assertEqual(response, mock_conversations_list)
        self.assertEqual(response2, "")
        self.assertEqual(options, mock_channel_list)
        client.conversations_list.assert_called_once()
        c.channel_list.assert_called_once()

    def test_choose_invite_option(self):
        options2 = ["Channel", "Invite Something", "Quit"]
        colors = MagicMock()
        client = MagicMock()
        c = MagicMock()
        ans = 1
        options = MagicMock()

        mock_users_list = MagicMock()
        client.users_list = MagicMock(return_value=mock_users_list)

        mock_user_list = MagicMock()
        c.user_list = MagicMock(return_value=mock_user_list)

        quit, response, response2, options = h.choose(options2, colors, client, c, ans, options)

        self.assertFalse(quit)
        self.assertEqual(response, mock_users_list)
        self.assertEqual(response2, mock_user_list)
        self.assertEqual(options, options)
        client.users_list.assert_called_once()
        c.user_list.assert_called_once()

    def test_choose_quit_option(self):
        options2 = ["Channel", "Invite Something", "Quit"]
        colors = MagicMock()
        client = MagicMock()
        c = MagicMock()
        ans = 2
        options = MagicMock()

        quit, response, response2, options = h.choose(options2, colors, client, c, ans, options)

        self.assertTrue(quit)
        self.assertEqual(response, "")
        self.assertEqual(response2, "")
        self.assertEqual(options, options)

    def test_choose_default_option(self):
        options2 = ["Channel", "Invite Something", "Quit", "default"]
        colors = MagicMock()
        client = MagicMock()
        c = MagicMock()
        ans = 3
        options = MagicMock()

        mock_users_list = MagicMock()
        client.users_list = MagicMock(return_value=mock_users_list)

        mock_user_list = MagicMock()
        c.user_list = MagicMock(return_value=mock_user_list)

        quit, response, response2, options = h.choose(options2, colors, client, c, ans, options)

        self.assertFalse(quit)
        self.assertEqual(response, mock_users_list)

if __name__ == '__main__':
    unittest.main()

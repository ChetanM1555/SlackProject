import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Initialize a Slack API client
client = WebClient(token=os.environ['xoxb-5417465273808-5399769040979-RPfmByTYfXPxfoGXlcO8pIMB'])

# Define the channel ID and bot user ID
channel_id = 'CHANNEL_ID'
bot_user_id = 'BOT_USER_ID'

try:
    # Invite the bot to the channel
    response = client.conversations_invite(channel=channel_id, users=bot_user_id)
    if response['ok']:
        print("Bot has been added to the channel successfully!")
    else:
        print("Failed to add bot to the channel.")
        print("Error:", response['error'])

except SlackApiError as e:
    print("Error adding bot to the channel:", e.response['error'])

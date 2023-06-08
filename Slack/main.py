from slack import WebClient
from simple_term_menu import TerminalMenu

# Create a WebClient instance using your API token
slack_token = "xoxb-5417465273808-5408907098545-rBcgkD4ZWMaFjBsYrignTkco"
client = WebClient(token=slack_token)

# Call the conversations.list method to retrieve the list of channels
response = client.conversations_list()

options = []

# Check if the API call was successful
if response["ok"]:
    # Iterate over the list of channels and print their IDs and names
    # print("------------------------------->") 
    for channel in response["channels"]:
        channel_id = channel["id"]
        channel_name = channel["name"]
        choice = f"{channel_name} - {channel_id}"
        options.append(choice)
        # print("Channel Name:", channel_name)
        # print("Channel ID:", channel_id)
        # print("------------------------------->")
else:
    print("Failed to retrieve channels. Error:", response["error"])

menu = TerminalMenu(options)
menu.show()

selected_index = menu.selected_option

# Handle user selection
selected_option = options[selected_index]
print("Selected option:", selected_option)

# Define the channel and message you want to send
channel_id = "C05BYBR2FAM"  # Replace with the actual channel ID
message = "Testing!!!!"

# # Send the message
# response = client.chat_postMessage(channel=channel_id, text=message)

# # Check if the message was sent successfully
# if response["ok"]:
#     print("Message sent successfully!")
# else:
#     print("Failed to send message. Error: ", response["error"])

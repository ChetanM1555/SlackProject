from slack_sdk.web import WebClient
from simple_term_menu import TerminalMenu
from colors import colors
import create_list as c

# Create a WebClient instance using your API token
while(True):
    
        slack_token = input(colors.GREEN + "Copy and paste your slack token here: \n" + colors.YELLOW)
        client = WebClient(token=slack_token)
        break
    

while (True):
    options2 = ["Channel","Direct Message","Quit"]
    options = []

    print(colors.GREEN + "Do you want to send to a channel or direct message: " + colors.YELLOW)
    menu = TerminalMenu(options2)
    ans = menu.show()

    if options2[ans] == "Channel":
        # Call the conversations.list method to retrieve the list of channels
        response = client.conversations_list()
        
        options = c.channel_list(options, response)
        
    elif options2[ans] == "Quit":
        print(colors.CYAN + "Noice!")
        break

    else:
        response = client.users_list()

        options = c.user_list(options, response)

    menu = TerminalMenu(options)
    selected_option = menu.show()

    # Handle user selection
    print(colors.CYAN + "Selected option:", options[selected_option])
    selected_option = options[selected_option]

    # Define the channel and message you want to send
    a = selected_option.split(" = ")

    channel_id = a[1]  # Replace with the actual channel ID
    message = input(colors.GREEN + "Enter a message: "+colors.YELLOW)


    # Send the message
    response = client.chat_postMessage(channel=channel_id, text=message)

    # Check if the message was sent successfully
    if response["ok"]:
        print(colors.GREEN + "Message sent successfully!")
    else:
        print(colors.RED + "Failed to send message. Error: ", response["error"])

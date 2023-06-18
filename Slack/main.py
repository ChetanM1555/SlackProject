from slack_sdk.web import WebClient
# from simple_term_menu import hgTerminalMenu
from colors import colors
import create_list as c

# Create a WebClient instance using your API token
while(True):
    
        slack_token = input(colors.BLUE + "Copy and paste your slack token here: \n" + colors.RESET)
        client = WebClient(token=slack_token)
        break
    

while (True):
    options2 = ["Channel","Direct Message","Invite Something","Quit"]
    options = []

    
    menu = TerminalMenu(options2)
    ans = menu.show()

    if options2[ans] == "Channel":
        print(colors.BLUE + "Do you want to send to a channel or direct message: " + colors.RESET)
        # Call the conversations.list method to retrieve the list of channels
        response = client.conversations_list()
        options = c.channel_list(options, response)

    elif options2 == "Invite Something":
         print("Who would you like to invite?")
         response = client.users_list()
         print("What channel would yoiu like to invite them to?")
        #  response2

        
    elif options2[ans] == "Quit":
        print(colors.BLUE + "Do you want to send to a channel or direct message: " + colors.RESET)
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
    message = input(colors.BLUE + "Enter a message: "+colors.RESET)


    # Send the message
    response = client.chat_postMessage(channel=channel_id, text=message)

    # Check if the message was sent successfully
    if response["ok"]:
        print(colors.GREEN + "Message sent successfully!")
    else:
        print(colors.PINK + "Failed to send message. Error: ", response["error"])

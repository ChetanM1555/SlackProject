from slack_sdk.web import WebClient
from simple_term_menu import TerminalMenu
from colors import colors
import choices as ch
import create_list as c
import config


# Create a WebClient instance using your API token
config.install_simple_term()
while(True):
    
        slack_token = input(colors.BLUE + "Copy and paste your slack token here: \n" + colors.PINK)
        client = WebClient(token=slack_token)
        break
    

while (True):
    options2 = ["Channel","Direct Message","Invite Something","Quit", "Create a channel"]
    options = []

    
    menu = TerminalMenu(options2)
    ans = menu.show()

    quit,response, response2, options =ch.choose(options2, colors, client, c, ans, options)
    

    if quit == True:
        break

    menu = TerminalMenu(options)
    selected_option = menu.show()

    # Handle user selection
    print(colors.CYAN + "Selected option:", options[selected_option])
    selected_option = options[selected_option]

    # Define the channel and message you want to send
    a = selected_option.split(" = ")
    print(options2[ans])
    if options2[ans] == "Invite Something":
        print("Where do you want to invite this person?")
        response = client.conversations_list()
        options=[]
        options = c.channel_list(options, response)
        menu = TerminalMenu(options)
        selected_option2 = menu.show()
        selected_option2 = options[selected_option2]
        selected_option2 = selected_option2.split(" = ")
        selected_option = selected_option.split(" = ")

        print(selected_option[1])
        print(selected_option2[1])
        r = client.conversations_invite(channel= selected_option2[1], users=selected_option[1])
    else:
        channel_id = a[1]  # Replace with the actual channel ID
        message = input(colors.BLUE + "Enter a message: "+colors.PINK)


        # Send the message
        response = client.chat_postMessage(channel=channel_id, text=message)

        # Check if the message was sent successfully
        if response["ok"]:
            print(colors.GREEN + "Message sent successfully!")
        else:
            print(colors.RED + "Failed to send message. Error: ", response["error"])

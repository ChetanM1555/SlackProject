from slack_sdk.web import WebClient
import slack_sdk
from simple_term_menu import TerminalMenu
from colors import colors
import choices
import create_list
import config


def run():
    while(True):
        # Create a WebClient instance using your API token
        slack_token = input(colors.BLUE + "Copy and paste your slack token here: \n" + colors.PINK)
        client = WebClient(token=slack_token)
        break
        
    
    while (True):
            try:
                options2 = ["Channel","Direct Message","Invite Something","Create a channel", "Quit"]
                options = []
                
                menu = TerminalMenu(options2)
                ans = menu.show()

                quit,response, response2, options =choices.choose(options2, client, create_list, ans)
                
                if quit == True:
                    break
                if(options2[ans]!="Create a channel"):
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
                        options = create_list.channel_list(options, response)
                        menu = TerminalMenu(options)
                        selected_option2 = menu.show()
                        selected_option2 = options[selected_option2]
                        selected_option2 = selected_option2.split(" = ")
                        selected_option = selected_option.split(" = ")

                        r = client.conversations_invite(channel= selected_option2[1], users=selected_option[1])
                        print(colors.BLUE+"Successfully invited to the channel")
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
            except slack_sdk.errors.SlackApiError as e:
                error_message = e.response["error"]
                print(colors.RED+"An error occurred:", error_message)


#############################################################################
x = input("Do you want to install simple term(y/n)?")
if x == "y": 
    config.install_simple_term()

# try:
run()
# except Exception as e:
#     print("An unexpected error occured, ending program...")

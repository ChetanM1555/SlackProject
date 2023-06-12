from slack_sdk.web import WebClient
from simple_term_menu import TerminalMenu

# Create a WebClient instance using your API token
slack_token = input("Copy and paste your slack token here: \n")
client = WebClient(token=slack_token)

while (True):
    options2 = ["Channel","Direct Message","Quit"]
    print("Do you want to send to a channel or direct message: ")
    menu = TerminalMenu(options2)
    ans = menu.show()
   
    if options2[ans] == "Channel":
        # Call the conversations.list method to retrieve the list of channels
        response = client.conversations_list()

        options = []
        
        # Check if the API call was successful
        if response["ok"]:
            # Iterate over the list of channels and print their IDs and names
            print("")
            for channel in response["channels"]:
                channel_id = channel["id"]
                channel_name = channel["name"]
                choice = f"{channel_name} = {channel_id}"
                options.append(choice)

        else:
            print("Failed to retrieve channels. Error:", response["error"])
    elif options2[ans] == "Quit":
        print("Noice!")
        break
    else:
        response = client.users_list()

        options = []

        if response["ok"]:

            for user in response["members"]:
                user_id = user["id"]
                user_name = user["real_name"] or user["name"]
                choice = f"{user_name} = {user_id}"
                options.append(choice)

    menu = TerminalMenu(options)
    selected_option = menu.show()

    # Handle user selection
    print("Selected option:", selected_option)
    selected_option = options[selected_option]

    # Define the channel and message you want to send
    a = selected_option.split(" = ")

    channel_id = a[1]  # Replace with the actual channel ID
    message = input("Enter a message: ")


    # Send the message
    response = client.chat_postMessage(channel=channel_id, text=message)

    # Check if the message was sent successfully
    if response["ok"]:
        print("Message sent successfully!")
    else:
        print("Failed to send message. Error: ", response["error"])

import slack_sdk
from colors import colors


def choose(options2,client, c, ans):
    options = []
    quit = False
    response = ""
    response2 = ""
    
    if options2[ans] == "Channel":
        print(colors.BLUE + "Do you want to send to a channel or direct message: " + colors.PINK)
        # Call the conversations.list method to retrieve the list of channels
        response = client.conversations_list()
        options = c.channel_list(options, response)

    elif options2[ans] == "Invite Something":
        print("Who would you like to invite?")
        response = client.users_list()
        response2 = c.user_list(options, response)
        # response2

        
    elif options2[ans] == "Quit":
        # print(colors.BLUE + "Do you want to send to a channel or direct message: " + colors.PINK)
        print(colors.CYAN + "Noice!")
        quit = True

    elif options2[ans] == "Create a channel":  
        try:
            print(colors.BLUE + "What do you want to name the channel: " + colors.PINK)
            myinput = input()
            response = client.conversations_create(
            name=myinput,
            is_private=False )
            channel = response["channel"]["name"]
            print(f"{channel} has been created")
        
        except slack_sdk.errors.SlackApiError as e:
            # Handle the specific error
            error_message = e.response["error"]
            if error_message == "invalid_name_specials":
                # Handle the 'invalid_name_specials' error
                print(colors.RED+"Invalid name with special characters.")
            else:
                # Handle other errors
                print(colors.RED+"An error occurred:", error_message)

    else:
        # Direct message option
        response = client.users_list()
        options = c.user_list(options, response)

    return quit, response, response2, options
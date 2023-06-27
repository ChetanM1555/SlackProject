def choose(options2,colors,client, c, ans, options):
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
        print(colors.BLUE + "Do you want to send to a channel or direct message: " + colors.PINK)
        print(colors.CYAN + "Noice!")
        quit = True
        

    else:
        # Direct message option
        response = client.users_list()
        options = c.user_list(options, response)

    return quit, response, response2, options
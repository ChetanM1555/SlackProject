from colors import colors

def channel_list(options, response):
    # Check if the API call was successful
        if response["ok"]:
            # Iterate over the list of channels and print their IDs and names
            print("")
            for channel in response["channels"]:
                channel_id = channel["id"]
                channel_name = channel["name"]
                # choice = f"{channel_name} = {channel_id}"
                choice = f"{colors.PURPLE}{channel_name} = {channel_id}"
                options.append(choice)
        else:
            print(colors.RED + "Failed to retrieve channels. Error:", response["error"])

        return options

def user_list(options, response):
    if response["ok"]:

        for user in response["members"]:
            user_id = user["id"]
            user_name = user["name"]
            # choice = f"{user_name} = {user_id}"
            choice = f"{colors.PURPLE}{user_name} = {user_id}"
            options.append(choice)
            
        return options
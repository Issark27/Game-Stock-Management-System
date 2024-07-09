def search(Search_Input):
    with open("Game_Info.txt", "r") as F:
        lines = F.readlines()
        
    game_dict = {}
    
    for line in lines[1:]:
        values = line.strip().split(",")
        game_id = values[0]
        game_info = values[1:5]
        
        #Dictionary has the games ID as a key and all the information as the value
        game_dict[game_id] = game_info
    
    game_availability = {}
    
    with open("Rental.txt", "r") as F:
        lines = F.readlines()
        
    for line in lines[1:]:
        values = line.strip().split(",")
        game_id = values[0]
        availability = values[2]
        #Dictionary has the games ID as a key and the availability as the value in which an empty string signifies it is not available
        game_availability[game_id] = availability

 
    found_games = []
    found_games_info = []
    found_games_availability = []
    
    for x, y in game_dict.items():
        for i in y:
            #Checks if the search input in lowercase is equal to any of the values in the array for a specfifc key
            if (Search_Input.lower() == i.lower()):
                found_games.append(x)
                found_games_info.append(y)
                for j,k in game_availability.items():
                    if (x == j):
                        found_games_availability.append(k)
                        break
                break
    
    #Checks if there is anything in the list     
    if len(found_games) != 0:
        print("Available Games based on your search:\n")
        for i in range (0, len(found_games)):
            print(f"Game ID: {found_games[i]}")
            print(f"Platform: {found_games_info[i][0]}")
            print(f"Genre: {found_games_info[i][1]}")
            print(f"Title: {found_games_info[i][2]}")
            print(f"Publisher: {found_games_info[i][3]}")
            if (found_games_availability[i] == ""):
                print("Availability: Unavailable\n")
            else:
                print("Availability: Available\n")
    else:
        print(f"\nNo Games found associated with the keyword '{Search_Input}'")
            

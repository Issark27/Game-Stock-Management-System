import feedbackManager

def Return(GID, Game_Review, Game_Comment, DATE):
    return_dict = {}
    #Name of all games
    names = []
    
    with open("Game_Info.txt", "r") as F:
        lines = F.readlines()
        
    for line in lines[1:]:
        values = line.strip().split(",")
        game_name = values[0]
        names.append(game_name)

 
    #Checks if game exists    
    if GID in names:
        with open("Game_Feedback.txt", "r") as F:
            lines = F.readlines()
            
        for line in lines[1:]:
            values = line.strip().split(",")
            game_id = values[0]
            game_feedback = values[1:3]
            return_dict[game_id] = game_feedback
 
    
        count = 0
    
        with open ("Rental.txt", "r") as F:
            lines = F.readlines()
        
        for i in range (1, len(lines)):
            values = lines[i].strip().split(",")
            game_id = values[0]
            game_return = values[2]
            customer_id = values[3]
        
            if (game_id == GID and game_return == ""):
                count = 1
                feedbackManager.add_feedback(GID, Game_Review, Game_Comment, "Game_Feedback.txt")
                print(f"'{GID}' has now been returned")
                #Changes the game_return date to the date inputted by user
                values[2] = DATE
                #Line now gets rewritten with the same information apart from the date
                lines[i] = f"{game_id},{values[1]},{DATE},{customer_id}\n"
                break
        

        with open("Rental.txt", "w") as F:
            F.writelines(lines)
        
        #If the games status is changed then count = 1 but if it is never changed then count = 0
        if count == 0:
            print(f"\nERROR: The game '{GID}' is already available")
            
    else:
        print(f"\nERROR: The game '{GID}' does not exist ")
        

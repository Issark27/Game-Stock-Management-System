import subscriptionManager as SM

def rent(CID, GID, DATE):
    game_list = []
    subscriptions = SM.load_subscriptions("Subscription_Info.txt")
    #Checks Subscription status of the customer
    subscription_status = SM.check_subscription(CID, subscriptions)
    
    #Code will only execute if subscription status is Premium (True)
    if (subscription_status == True):
        print("Subscription Status Premium: Able to Rent")
        
        with open("Rental.txt", "r") as F:
            x = F.readlines()
        
        #rent_dict stores the keys of the game and whether its return date (if return date is empty it is still being rented)
        rent_dict = {}
        #limit_dict stores the customer ID and whther their last return date is empty (still renting) or not
        limit_dict = {}
        
        for line in x[1:]:
            values = line.strip().split(",")
            customer_id = values[3]
            game = values[0]
            game_availability = values[2]
            rent_dict[game] = game_availability
            limit_dict[customer_id] = game_availability
            game_list.append(game) 
        
        rent_list = []
        with open("Game_Info.txt", "r") as F:
            y = F.readlines()
        for line in y[1:]:
            values = line.strip().split(",")
            game = values[0]
            rent_list.append(game)
            
        #Checks if game exists
        if (GID in rent_list):
            if (CID in limit_dict and limit_dict[CID] == ""):
                print(f"\nERROR: '{CID}' is already renting a game")
            else:
                for i in rent_list:
                    if (i == GID and (GID in rent_dict.keys())):
                        value = rent_dict[GID]
                        #Case when return date is empty and so is still being rented
                        if (value == ''):
                            print(f"\nERROR: '{GID}' is still being rented\n")
                            break
                        #Case when return date is not empty so it is still available
                        else:
                            print(f"\n'{GID}' has been rented\n")
                            with open("Rental.txt", "a") as F:
                                #Writes to file in correct format
                                F.write(f"{GID},{DATE},,{CID}\n")
                                break
                    elif (i == GID and (GID not in rent_dict.keys())):
                        print(f"\n{GID} has been rented\n")
                        with open("Rental.txt", "a") as F:
                            F.write(f"{GID},{DATE},,{CID}\n")
                            break

        else:
            print(f"\nERROR: The game '{GID}' does not exist")
                
    elif (subscription_status == False):
        print("\nERROR: Unable to rent as Subscription Status is Basic\n")
    


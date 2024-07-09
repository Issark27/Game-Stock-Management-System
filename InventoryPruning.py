import feedbackManager
import matplotlib.pyplot as plt
plt.style.use("ggplot")

def stats():
    with open ("Rental.txt", "r") as F:
        lines = F.readlines()
        
    game_list = []
        
    for line in lines[1:]:
        values = line.strip().split(",")
        game_id = values[0]
        game_list.append(game_id)
    
    #Counts the amount of times a game ID has been rented 
    count_dict = {}
    
    for i in game_list:
        count = 0
        for x in range(0, len(game_list)):
            if (i == game_list[x]):
                count = count + 1
                count_dict[i] = count

                
    with open ("Game_Info.txt", "r") as F:
        lines = F.readlines()
    
    #Stores the game ID as the key and the title as the value    
    game_name = {}
    
    for line in lines[1:]:
        values = line.strip().split(",")
        game_id = values[0]
        title = values[3]
        game_name[game_id] = title
        
        
    
    updated_dict = {}
    #Checks the elements in the total game ID list
    for i in game_list:
        #Checks if the game ID is in the game_id dict key
        if i in game_name:
            #It then saves the value of the game_name (title)
            x = game_name[i]
            #If the key (title) is already in updated_dict then it will increment it
            if x in updated_dict:
                updated_dict[x] += 1
            #Otherwise if the title is not already in the updated_dict it will not be put with a value of 1
            else:
                updated_dict[x] = 1
                     
                    
    with open ("Game_Feedback.txt", "r") as F:
        lines = F.readlines()
    
    game_feedback = {}
    game_feedback_updated = {}

    for line in lines[1:]:
        values = line.strip().split(",")
        game_id = values[0]
        game_rating = values[1]
        
        #Finds the sum of the game ratings
        if game_id in game_feedback.keys():
            game_feedback[game_id] += int(game_rating)
        else:
            game_feedback[game_id] = int(game_rating)
        
    
    for i,j in game_feedback.items():
        for x,y in game_name.items():
            if (i == x):
                #Finds the sum of the game ratings but uses the title instead of game ID
                if y in game_feedback_updated:
                    game_feedback_updated[y] += int(j)
                else:
                    game_feedback_updated[y] = int(j)
    
    counter = {}
    counter_updated = {}
    
    with open ("Game_Feedback.txt", "r") as F:
        lines = F.readlines()
        
    for line in lines[1:]:
        letters = line[:3]
        
        #Checks the amount of times the same name appeared using the first 3 letters and used this to find the number of times it has been rented
        if letters in counter:
            counter[letters] += 1
        else:
            counter[letters] = 1
 
    for i,j in counter.items():
        for x,y in game_name.items():
            #Creates new counter dict where the key is the title and the value is the number of times it has been rented
            if (i == x[:3].lower()):
                counter_updated[y] = j
    
    averages = {}
    
    for i in counter_updated:
        if i in game_feedback_updated:
            #Finds the mean of the rating by dividing the sum of the ratings by the number of times it has been rented
            averages[i] = round(float(game_feedback_updated[i] / counter_updated[i]), 2)
            
                                
    
    x_axis_rentals = list(updated_dict.keys())
    y_axis_rentals = list(updated_dict.values())
    
    fig, axes =  plt.subplots(nrows = 1, ncols = 2, figsize = (16, 6))
    
    colours_rentals = ["skyblue" if value > 14 else "lightgreen" if value > 10 else "lightcoral" for value in y_axis_rentals]
    axes[0].barh(x_axis_rentals, y_axis_rentals, height = 0.25, color = colours_rentals)
    axes[0].set_xlim(0, 20)
    axes[0].set_title("Number of Rentals per Game")
    axes[0].set_ylabel("Game Name")
    axes[0].set_xlabel("Number of Rentals")
    axes[0].set_xticks(range(0, 21, 5))
    rental_colour = {"Most Popular Rentals":"skyblue", "High Rentals":"lightgreen", "Low Rentals":"lightcoral"}
    labels = list(rental_colour.keys())
    handles = [plt.Rectangle((0,0),1,1, color = rental_colour[label]) for label in labels]
    axes[0].legend(handles,labels)
    
    
    x_axis_rating = list(averages.keys())
    y_axis_rating = list(averages.values())
    
    colours_ratings = ["skyblue" if value >=  4 else "lightgreen" if value > 3 else "lightcoral" for value in y_axis_rating]
    axes[1].barh(x_axis_rating, y_axis_rating, height = 0.25, color = colours_ratings)
    axes[1].set_title("Average Game Ratings")
    axes[1].set_ylabel("Game Name")
    axes[1].set_xlabel("Game Rating")
    axes[1].set_xticks(range(0, 6, 1))
    rating_colour = {"Highest Ratings":"skyblue", "Good Ratings":"lightgreen", "Low Ratings":"lightcoral"}
    labels1 = list(rating_colour.keys())
    handles1 = [plt.Rectangle((0,0),1,1, color = rating_colour[label]) for label in labels1]
    axes[1].legend(handles1,labels1)
    
    plt.tight_layout()
    plt.show()
    
    for i,j in averages.items():
        if i in updated_dict:
            rentals = int(updated_dict[i])
            if int(j) < 3 and rentals < 8:
                print(f"The game '{i}' has an average rating of '{j}' and has been rented only '{rentals}' times. It could be considered for pruning action.\n")
            

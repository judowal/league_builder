# import csv module
import csv

# create a list for each team
dragons = []
sharks = []
raptors = []

# create a list of all drafted players
drafted = []

# create a list of experienced players
experienced = []

# create list of inexperienced players
inexperienced = []

# list of lists containing team list and team name
teams = [[dragons, "Dragons"], [sharks, "Sharks"], [raptors, "Raptors"]]


# convert csv into list of lists
def csv_converter(file_name):

    # open csv file for reading
    with open(file_name + ".csv", newline="") as csv_file:

        # reads csv file
        player_reader = csv.reader(csv_file, delimiter=",")

        # converts csv data to list of lists
        player_data = list(player_reader)

    # function returns list of lists containing category titles and player data
    return player_data


# convert list of lists to list of dictionaries
def player_lister():

    # reads csv file and stores list of lists
    player_info = csv_converter("soccer_players")

    # list of all players
    # each player is a dictionary
    players = []

    # set k to 1 to start loop at first player
    # item 0 in player_info is category titles (Name, Height, Experienced, etc.)
    k = 1

    # for each category title in player_info
    # skips first list item to skip category titles
    for _ in player_info[1:]:

        # create new dictionary to represent player
        player = {}

        # set i to 0 to start at first item of player information (player name, player height, experience level, etc.)
        i = 0

        # for each item of player information
        for _ in player_info[0]:

            # add new entry to player dictionary
            player[_] = player_info[k][i]

            # increment i to move to next list item
            i += 1
        # increment k to move to next player
        k += 1

        # add player to list of players
        players.append(player)

    # function returns list of players
    return players


# gather all experienced players
def experienced_players():

    # for each player in list of players
    for player in player_lister():

        # if player has soccer experiences
        if player['Soccer Experience'] == "YES" and player not in experienced:

            # add player to list of experienced players
            experienced.append(player)

    # function returns list of experienced players
    return experienced


# gather all inexperienced players
def inexperienced_players():

    # for each player in list of players
    for player in player_lister():

        # if player does not have soccer experience
        if player['Soccer Experience'] == "NO" and player not in inexperienced:

            # add player to list of inexperienced players
            inexperienced.append(player)

    # function returns list of inexperienced players
    return inexperienced


# draft player
def drafter(team, player):

    # add player to team list
    team[0].append(player)

    # add player to list of drafted players
    drafted.append(player)


# distribute experienced players evenly
def experienced_drafter(team):

    # for each player in list of experienced players
    for player in experienced_players():

        # if player is not in list of drafted players
        if player not in drafted:

            # if team's length is less than number of experienced players divided by number of teams
            if len(team[0]) < len(experienced_players()) / len(teams):

                # add player to team list and drafted list
                drafter(team, player)


# distribute inexperienced players
def inexperienced_drafter(team):

    # for each player in inexperienced players
    for player in inexperienced_players():

        # if player is not in list of drafted players
        if player not in drafted:

            # if team's length is less than number of players divided by number of teams
            if len(team[0]) < len(player_lister()) / len(teams):

                # add player to team list and drafted list
                drafter(team, player)


# adds team entry to player dictionary
# accepts team as argument
def team_labeler(team):

    # for each player on the team
    for player in team[0]:

        # create a new entry in the player's dictionary
        player["Team"] = team[1]


# prints the roster
def roster_printer(team, file):

    # write team name and divider to file
    file.write("{}\n".format(team[1]) + len(team[1]) * "=" + "\n")

    # for each player on the team
    for player in team[0]:

        # for each key value pair in player dictionary
        for key, value in player.items():

            # if the current key equals team
            if key == "Team":

                # write team's value to file
                file.write(value)

            # if current key does not equal team
            else:

                # write the value followed by a comma and a space
                file.write(value + ", ")

        # write newline after each player's information is written to file
        file.write("\n")

    # write newline after each team is written to file
    file.write("\n")


# print a letter for each player
def letter_printer():

    # for each player in list of drafted players
    for player in drafted:

        # open player letter file for writing
        with open(player['Name'] + ".txt", "w") as player_file:

            # write letter to file
            player_file.write("Dear {}, \n\n".format(player['Guardian Name(s)']))
            player_file.write("Player Name: {}\n".format(player['Name']))
            player_file.write("Player Team: {}\n\n".format(player['Team']))
            player_file.write("Hello and welcome to the summer soccer league.\n")
            player_file.write("The first practice is August 11, 2018 @ 2:00pm.\n")
            player_file.write("Lunch will be provided.\n")
            player_file.write("Practice ends at roughly 6:00pm.\n")
            player_file.write("\nThank you.")


# run the application
def app():

    # open roster file for writing
    with open("teams.txt", "w") as team_file:

        # for each team in list of teams
        for team in teams:

            # draft experienced players
            experienced_drafter(team)

            # draft inexperienced players
            inexperienced_drafter(team)

            # print team roster to file
            roster_printer(team, team_file)

        for team in teams:
            # add team to dictionary
            team_labeler(team)

        # print a letter for each player
        letter_printer()


# if the name of this file is __main__
if __name__ == "__main__":

    # run app
    app()

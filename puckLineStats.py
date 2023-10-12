import requests
from prettytable import PrettyTable

# Function to fetch franchise data
def fetch_franchise_data():
    api_url = "https://statsapi.web.nhl.com/api/v1/franchises/10"
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

# Function to fetch team data
def fetch_team_data():
    api_url = "https://statsapi.web.nhl.com/api/v1/teams/3"
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

# Function to fetch roster data and player IDs
def fetch_roster_data():
    api_url = "https://statsapi.web.nhl.com/api/v1/teams/3/roster"
    response = requests.get(api_url)
    response.raise_for_status()
    roster_data = response.json()['roster']
    player_ids = {player['person']['fullName']: player['person']['id'] for player in roster_data}
    return roster_data, player_ids

# Function to fetch upcoming game data
def fetch_upcoming_game_data():
    api_url = "https://statsapi.web.nhl.com/api/v1/teams/3?expand=team.schedule.next"
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

# Function to fetch player data based on player ID
# Function to fetch player data based on player ID
def fetch_player_data(player_id):
    api_url = f"https://statsapi.web.nhl.com/api/v1/people/{player_id}"
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

# Function to get player ID based on name
def get_player_id_by_name(player_name):
    api_url = f"https://statsapi.web.nhl.com/api/v1/teams/3/roster"
    response = requests.get(api_url)
    response.raise_for_status()
    roster_data = response.json()['roster']
    for player in roster_data:
        if player['person']['fullName'] == player_name:
            return player['person']['id']
    return None

# Function to compare two players' stats
def compare_players(player1_name, player2_name):
    player1_id = get_player_id_by_name(player1_name)
    player2_id = get_player_id_by_name(player2_name)

    print(f"Player 1 ID: {player1_id}")
    print(f"Player 2 ID: {player2_id}")

    if player1_id and player2_id:
        player1_stats = fetch_player_data(player1_id)
        player2_stats = fetch_player_data(player2_id)

        # Print the retrieved names
        print(f"Player 1 Name: {player1_stats['people'][0]['fullName']}")
        print(f"Player 2 Name: {player2_stats['people'][0]['fullName']}")
        # Create PrettyTable for comparison
        table = PrettyTable()
        table.field_names = ['Attribute', player1_name, player2_name]

        # Attributes to compare
        attributes_to_compare = ['fullName', 'primaryNumber', 'birthDate', 'height', 'weight', 'position']

        for attribute in attributes_to_compare:
            player1_value = player1_stats['people'][0].get(attribute, 'N/A')
            player2_value = player2_stats['people'][0].get(attribute, 'N/A')
            table.add_row([attribute, player1_value, player2_value])

        # Print the table
        print(table)
    else:
        print("Invalid player names.")

# Main program loop
while True:
    print("Select an option:")
    print("1. Get General Franchise Info")
    print("2. Get General Team Info")
    print("3. Get Roster Info")
    print("4. Get Upcoming Game Info")
    print("5. Player Comparison")

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        data = fetch_franchise_data()
        print(f"Team Name: {data['franchises'][0]['teamName']}")
        print(f"Location Name: {data['franchises'][0]['locationName']}")
    elif user_choice == 2:
        data = fetch_team_data()
        print(f"Team Name: {data['teams'][0]['name']}")
        print(f"City: {data['teams'][0]['locationName']}")
        print(f"Venue Name: {data['teams'][0]['venue']['name']}")
        print(f"First Year of Play: {data['teams'][0]['firstYearOfPlay']}")
        print(f"Division Name: {data['teams'][0]['division']['name']}")
        print(f"Conference Name: {data['teams'][0]['conference']['name']}")
    elif user_choice == 3:
        roster_data, player_ids = fetch_roster_data()
        for player in roster_data:
            print(f"Full Name: {player['person']['fullName']}")
            print(f"Player ID: {player['person']['id']}")
            print("------")
    elif user_choice == 4:
        data = fetch_upcoming_game_data()
        game = data['teams'][0]['nextGameSchedule']['dates'][0]['games'][0]
        away_team = game['teams']['away']['team']['name']
        home_team = game['teams']['home']['team']['name']
        print(f"Game Date: {game['gameDate']}")
        print(f"Away Team: {away_team}")
        print(f"Home Team: {home_team}")
    elif user_choice == 5:
        roster_data, player_ids = fetch_roster_data()

        # Print roster data for player selection
        for player in roster_data:
            print(f"Full Name: {player['person']['fullName']}")
            print(f"Player ID: {player['person']['id']}")
            print("------")

        # Prompt user to select players for comparison
        player1_name = input("Enter the full name of Player 1: ")
        player2_name = input("Enter the full name of Player 2: ")

        compare_players(player1_name, player2_name)
    
    another_option = input("Do you want to choose another option? (yes/no): ").lower()
    if another_option != 'yes':
        print("Thanks checking out my stat tracker for the NY Rangers")
        break

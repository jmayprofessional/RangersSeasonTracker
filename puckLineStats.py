import requests

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
    roster_data = response.json()
    player_ids = {}
    for player in roster_data['roster']:
        full_name = player['person']['fullName']
        player_id = player['person']['id']
        player_ids[full_name] = player_id
    return roster_data, player_ids

# Function to fetch upcoming game data
def fetch_upcoming_game_data():
    api_url = "https://statsapi.web.nhl.com/api/v1/teams/3?expand=team.schedule.next"
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

# Function to fetch player data based on player ID
def fetch_player_data(player_id):
    api_url = f"https://statsapi.web.nhl.com/api/v1/people/{player_id}/stats?stats=statsSingleSeason&season=20222023"
    response = requests.get(api_url)
    response.raise_for_status()
    player_stats = response.json()['stats'][0]['splits'][0]['stat']

    # Extract player stats
    games = player_stats['games']
    time_on_ice = player_stats['timeOnIce']
    even_time_on_ice = player_stats['evenTimeOnIce']
    goals = player_stats['goals']
    assists = player_stats['assists']
    shots = player_stats['shots']
    hits = player_stats['hits']
    plus_minus = player_stats['plusMinus']
    points = player_stats['points']
    power_play_goals = player_stats['powerPlayGoals']
    power_play_points = player_stats['powerPlayPoints']
    power_play_time_on_ice = player_stats['powerPlayTimeOnIce']
    penalty_minutes = player_stats['penaltyMinutes']
    face_off_pct = player_stats['faceOffPct']
    shot_pct = player_stats['shotPct']
    game_winning_goals = player_stats['gameWinningGoals']
    overtime_goals = player_stats['overTimeGoals']
    shorthanded_goals = player_stats['shortHandedGoals']
    shorthanded_points = player_stats['shortHandedPoints']
    time_on_ice_per_game = player_stats['timeOnIcePerGame']

    # Print player stats
    print(f"Games: {games}")
    print(f"Time on Ice: {time_on_ice}")
    print(f"Even Strength Time on Ice: {even_time_on_ice}")
    print(f"Goals: {goals}")
    print(f"Assists: {assists}")
    print(f"Shots: {shots}")
    print(f"Hits: {hits}")
    print(f"Plus-Minus: {plus_minus}")
    print(f"Points: {points}")
    print(f"Power Play Goals: {power_play_goals}")
    print(f"Power Play Points: {power_play_points}")
    print(f"Power Play Time on Ice: {power_play_time_on_ice}")
    print(f"Penalty Minutes: {penalty_minutes}")
    print(f"Face-off Percentage: {face_off_pct}")
    print(f"Shot Percentage: {shot_pct}")
    print(f"Game-Winning Goals: {game_winning_goals}")
    print(f"Overtime Goals: {overtime_goals}")
    print(f"Shorthanded Goals: {shorthanded_goals}")
    print(f"Shorthanded Points: {shorthanded_points}")
    print(f"Time on Ice Per Game: {time_on_ice_per_game}")

# Main program loop
while True:
    print("Select an option:")
    print("1. Get General Franchise Info")
    print("2. Get General Team Info")
    print("3. Get Roster Info")
    print("4. Get Upcoming Game Info")

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        data = fetch_franchise_data()
        franchise_info = data['franchises'][0]
        print(f"Team Name: {franchise_info['teamName']}")
        print(f"Location Name: {franchise_info['locationName']}")
    elif user_choice == 2:
        data = fetch_team_data()
        team_info = data['teams'][0]
        print(f"Team Name: {team_info['name']}")
        print(f"City: {team_info['locationName']}")
        print(f"Venue Name: {team_info['venue']['name']}")
        print(f"First Year of Play: {team_info['firstYearOfPlay']}")
        print(f"Division Name: {team_info['division']['name']}")
        print(f"Conference Name: {team_info['conference']['name']}")
    elif user_choice == 3:
        roster_data, player_ids = fetch_roster_data()
        for player in roster_data['roster']:
            print(f"Full Name: {player['person']['fullName']}")
            print(f"Jersey Number: {player['jerseyNumber']}")
            print(f"Position Name: {player['position']['name']}")
            print("------")
        
        view_individual_player = input("Do you want to select an individual player? (yes/no): ").lower()
        if view_individual_player == 'yes':
            full_name = input("Enter the player's full name: ")
            if full_name in player_ids:
                player_id = player_ids[full_name]
                fetch_player_data(player_id)
            else:
                print("Player not found in the roster.")
    elif user_choice == 4:
        data = fetch_upcoming_game_data()
        game = data['teams'][0]['nextGameSchedule']['dates'][0]['games'][0]
        away_team = game['teams']['away']['team']['name']
        home_team = game['teams']['home']['team']['name']
        print(f"Game Date: {game['gameDate']}")
        print(f"Away Team: {away_team}")
        print(f"Home Team: {home_team}")
    else:
        print("Invalid choice. Please select a valid option.")
    
    another_option = input("Do you want to choose another option? (yes/no): ").lower()
    if another_option != 'yes':
        print("Thanks for checking out my New York Rangers Stat tracker built with python")

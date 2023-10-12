import requests

def fetch_franchise_data():
    api_url = "https://statsapi.web.nhl.com/api/v1/franchises/10"
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def fetch_team_data():
    api_url = "https://statsapi.web.nhl.com/api/v1/teams/3"
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def fetch_roster_data():
    api_url = "https://statsapi.web.nhl.com/api/v1/teams/3/roster"
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def fetch_upcoming_game_data():
    api_url = "https://statsapi.web.nhl.com/api/v1/teams/3?expand=team.schedule.next"
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

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
        data = fetch_roster_data()
        for player in data['roster']:
            print(f"Full Name: {player['person']['fullName']}")
            print(f"Jersey Number: {player['jerseyNumber']}")
            print(f"Position Name: {player['position']['name']}")
            print("------")
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
        print("Thanks for checking out my New York Rangers Stat tracker built with python, Come back soon or give me a really cool job dealing with analytics! Thanks again and have a great season!")
        break

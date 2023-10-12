import requests

def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        
        # Parse the JSON data from the response
        data = response.json()
        return data
        
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")

# Dictionary mapping user choices to API endpoints
api_endpoints = {
    1: "https://statsapi.web.nhl.com/api/v1/franchises/10",
    2: "https://statsapi.web.nhl.com/api/v1/teams/3",
    3: "https://statsapi.web.nhl.com/api/v1/teams/3/roster",
    4: "https://statsapi.web.nhl.com/api/v1/teams/3?expand=team.schedule.next"
    # Add more options as needed
}

# Display options to the user
print("Select an option:")
print("1. Get General Franchise Info")
print("2. Get General Team Info")
print("3. Get Roster Info")
print("4. Get Upcoming Game Info")

# Take user input for choice
user_choice = int(input("Enter your choice: "))

# Check user choice and execute corresponding API call
if user_choice in api_endpoints:
    api_url = api_endpoints[user_choice]
    data = fetch_data(api_url)

    # Process and print the fetched data based on user choice
    if user_choice == 1 and 'franchises' in data:
        franchise_info = data['franchises'][0]
        team_name = franchise_info.get('teamName', 'N/A')
        location_name = franchise_info.get('locationName', 'N/A')
        print(f"Team Name: {team_name}")
        print(f"Location Name: {location_name}")
    elif user_choice == 2 and 'teams' in data:
        team_info = data['teams'][0]
        name = team_info.get('name', 'N/A')
        city = team_info.get('locationName', 'N/A')
        venue_name = team_info.get('venue', {}).get('name', 'N/A')
        first_year_of_play = team_info.get('firstYearOfPlay', 'N/A')
        division_name = team_info.get('division', {}).get('name', 'N/A')
        conference_name = team_info.get('conference', {}).get('name', 'N/A')
        
        print(f"Team Name: {name}")
        print(f"City: {city}")
        print(f"Venue Name: {venue_name}")
        print(f"First Year of Play: {first_year_of_play}")
        print(f"Division Name: {division_name}")
        print(f"Conference Name: {conference_name}")
    elif user_choice == 3 and 'roster' in data:
        roster = data['roster']
        for player in roster:
            full_name = player.get('person', {}).get('fullName', 'N/A')
            jersey_number = player.get('jerseyNumber', 'N/A')
            position_name = player.get('position', {}).get('name', 'N/A')
            print(f"Full Name: {full_name}")
            print(f"Jersey Number: {jersey_number}")
            print(f"Position Name: {position_name}")
            print(f"------")
    elif user_choice == 4 and 'teams' in data:
        next_game = data['teams'][0].get('nextGameSchedule', {}).get('dates', [])[0]
        if next_game:
            game_date = next_game.get('date', 'N/A')
            away_team = next_game.get('games', [])[0].get('teams', {}).get('away', {}).get('team', {}).get('name', 'N/A')
            home_team = next_game.get('games', [])[0].get('teams', {}).get('home', {}).get('team', {}).get('name', 'N/A')
            away_wins = next_game.get('games', [])[0].get('teams', {}).get('away', {}).get('leagueRecord', {}).get('wins', 'N/A')
            away_losses = next_game.get('games', [])[0].get('teams', {}).get('away', {}).get('leagueRecord', {}).get('losses', 'N/A')
            away_ot = next_game.get('games', [])[0].get('teams', {}).get('away', {}).get('leagueRecord', {}).get('ot', 'N/A')
            home_wins = next_game.get('games', [])[0].get('teams', {}).get('home', {}).get('leagueRecord', {}).get('wins', 'N/A')
            home_losses = next_game.get('games', [])[0].get('teams', {}).get('home', {}).get('leagueRecord', {}).get('losses', 'N/A')
            home_ot = next_game.get('games', [])[0].get('teams', {}).get('home', {}).get('leagueRecord', {}).get('ot', 'N/A')
            
            print(f"Game Date: {game_date}")
            print(f"Away Team: {away_team}")
            print(f"Away Team League Record - Wins: {away_wins}, Losses: {away_losses}, OT: {away_ot}")
            print(f"Home Team: {home_team}")
            print(f"Home Team League Record - Wins: {home_wins}, Losses: {home_losses}, OT: {home_ot}")
        else:
            print("No upcoming game information available.")
    elif data:
        print("Fetched Data:")
        print(data)
    else:
        print("No valid data found in the API response.")
else:
    print("Invalid choice. Please select a valid option.")

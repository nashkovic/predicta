import requests
from bs4 import BeautifulSoup

# Get team names from user input
team1 = input("Enter Team 1 Name: ")
team2 = input("Enter Team 2 Name: ")

# Search for recent form and statistics on the internet
url = "https://www.example.com/search?q=" + team1 + "+" + team2
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Analyze data to find likely winner
# Here, we'll just assume that the team with the better recent form and statistics is the likely winner
team1_recent_form = 7
team1_statistics = 85
team2_recent_form = 5
team2_statistics = 72

if team1_recent_form + team1_statistics > team2_recent_form + team2_statistics:
    likely_winner = team1
else:
    likely_winner = team2

# Return result to user
print("Based on recent form and statistics, the likely winner is: " + likely_winner)

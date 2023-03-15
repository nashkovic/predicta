import pandas as pd

def predict_winner(team1, team2):
    # Load the data for both teams
    team1_data = pd.read_csv(f'data/{team1}.csv')
    team2_data = pd.read_csv(f'data/{team2}.csv')

    # Calculate the recent form of each team
    team1_form = team1_data['Result'].tail(5).value_counts(normalize=True).get('W', 0)
    team2_form = team2_data['Result'].tail(5).value_counts(normalize=True).get('W', 0)

    # Calculate the overall statistics for each team
    team1_stats = team1_data.describe().loc[['mean', 'std', 'min', 'max']].to_dict()
    team2_stats = team2_data.describe().loc[['mean', 'std', 'min', 'max']].to_dict()

    # Combine the form and statistics into a single dictionary
    team1_dict = {'form': team1_form, 'stats': team1_stats}
    team2_dict = {'form': team2_form, 'stats': team2_stats}

    # Determine the likely winner based on the form and statistics
    if team1_form > team2_form:
        winner = team1
    elif team2_form > team1_form:
        winner = team2
    else:
        if team1_stats['Goals']['mean'] > team2_stats['Goals']['mean']:
            winner = team1
        elif team2_stats['Goals']['mean'] > team1_stats['Goals']['mean']:
            winner = team2
        else:
            winner = 'Draw'

    # Return the winner as a string
    return winner

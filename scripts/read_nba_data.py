import os
import sys
import pandas as pd


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Read NBA data from data file
player_stats = pd.read_csv('data/2017-18_playerBoxScore.csv',
						   parse_dates=['gmDate'])
team_stats = pd.read_csv('data/2017-18_teamBoxScore.csv',
						 parse_dates=['gmDate'])
standings = pd.read_csv('data/2017-18_standings.csv',
						parse_dates=['stDate'])

# Western Confence
west_top_2 = (standings[(standings['teamAbbr'] == 'HOU') |
			 (standings['teamAbbr'] == 'GS')]
			 .loc[:, ['stDate', 'teamAbbr', 'gameWon']]
			 .sort_values(['teamAbbr', 'stDate']))

# Find all players who shot a 3
three_takers = player_stats[player_stats['play3PA'] > 0]

# One column of players
three_takers['name'] = [f'{p["playFNm"]} {p["playLNm"]}'
						for _, p in three_takers.iterrows()]

# Total three_point attempts and makes
three_takers = (three_takers.groupby('name')
							.sum()
							.loc[:,['play3PA', 'play3PM']]
							.sort_values('play3PA', ascending=False))

# Filter out low volume shooters
three_takers = three_takers[three_takers['play3PA'] >= 100]

# Three point percentage
three_takers['pct3PM'] = three_takers['play3PM'] / three_takers['play3PA']

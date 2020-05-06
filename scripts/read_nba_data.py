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


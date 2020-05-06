from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.layouts import column, row
from bokeh.plotting import figure, show

from read_nba_data import *


output_file('east_and_west_top_2_standings_race.html',
			title='Conference Top 2 Teams Wins')

# Isolate the Rockets and the Warriors
standings_data = ColumnDataSource(standings)

# Create ColumnDataSources
celtics_view = CDSView(source=standings_data,
					   filters=[GroupFilter(column_name='teamAbbr', group='BOS')])
raptors_view = CDSView(source=standings_data,
					   filters=[GroupFilter(column_name='teamAbbr', group='TOR')])
rockets_view = CDSView(source=standings_data,
					   filters=[GroupFilter(column_name='teamAbbr', group='HOU')])
warriors_view = CDSView(source=standings_data,
					   filters=[GroupFilter(column_name='teamAbbr', group='GS')])

# Create figure
east_fig = figure(x_axis_type='datetime',
			 	  plot_height=300,
			  	  plot_width=600,
			 	  title='Eastern Conference Top 2 Teams Wins',
			 	  toolbar_location=None)
west_fig = figure(x_axis_type='datetime',
			 	  plot_height=300,
			  	  plot_width=600,
			 	  title='Western Conference Top 2 Teams Wins',
			 	  toolbar_location=None)

# Render specs
east_fig.step('stDate',
			  'gameWon',
		  	  color='#007A33',
		 	  legend_label='Celtics',
		 	  source=standings_data,
		 	  view=celtics_view)
east_fig.step('stDate',
		 	  'gameWon',
		 	  color='#CE1141',
		 	  legend_label='Toronto',
		 	  source=standings_data,
		 	  view=raptors_view)
west_fig.step('stDate',
	 		  'gameWon',
		  	  color='#CE1141',
		 	  legend_label='Rockets',
		 	  source=standings_data,
		 	  view=rockets_view)
west_fig.step('stDate',
		 	  'gameWon',
		 	  color='#006BB6',
		 	  legend_label='Warriors',
		 	  source=standings_data,
		 	  view=warriors_view)

east_fig.legend.location = 'top_left'
west_fig.legend.location = 'top_left'

show(column(west_fig, east_fig))
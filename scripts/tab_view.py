from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.plotting import figure, show
from bokeh.models.widgets import Tabs, Panel

from read_nba_data import *


output_file('east_and_west_top_2_tabbed.html',
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

# Reduce the width
east_fig.plot_width = west_fig.plot_width = 800

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

# Create panels
east_panel = Panel(child=east_fig, title='Eastern Conference')
west_panel = Panel(child=west_fig, title='Western Conference')

# Create Tabs
tabs = Tabs(tabs=[west_panel, east_panel])

show(tabs)

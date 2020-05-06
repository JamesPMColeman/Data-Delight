from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter


from read_nba_data import *


output_file('west_top_2_standings_race.html',
			title='Western Conference Top 2 Teams Wins')

# Creat ColumnDataSource
west_data = ColumnDataSource(west_top_2)

# Create view for each team
rockets_view = CDSView(source=west_data,
					   filters=[GroupFilter(column_name='teamAbbr', group='HOU')])
warriors_view = CDSView(source=west_data,
					   filters=[GroupFilter(column_name='teamAbbr', group='GS')])

# Create figure
west_fig = figure(x_axis_type='datetime',
				 plot_height=300,
				 plot_width=600,
				 title='Western Conference Top 2 Teams Wins',
			 	 toolbar_location=None)

# Render specs
west_fig.step('stDate',
		 	  'gameWon',
		 	  source=west_data,
		 	  view=rockets_view,
		 	  color='#CE1141',
		 	  legend_label='rockets')

west_fig.step('stDate',
		 	  'gameWon',
		 	  source=west_data,
		 	  view=warriors_view,
		 	  color='#006BB6',
		 	  legend_label='warriors')
		 

west_fig.legend.location = 'top_left'

show(west_fig)
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CategoricalColorMapper, Div, HoverTool
from bokeh.layouts import gridplot, column 
from bokeh.plotting import figure, show

from read_nba_data import nuggets

output_file('nugget_stats.html', title='Nuggets Statistics')

nugget_stats = ColumnDataSource(nuggets)

# Create categorical color mapper
win_loss_mapper = CategoricalColorMapper(factors = ['W', 'L'],
										  palette=['green', 'red'])

hover_info = [('Opponent', '@opptAbbr')]

stat_names = {'Points': 'teamPTS',
			  'Assists': 'teamAST',
			  'Rebounds': 'teamTRB',
			  'Turnovers': 'teamTO'}

stat_figs = {}

for stat_label, stat_col in stat_names.items():

	# Create a figure
	fig = figure(y_axis_label=stat_label,
				 plot_height=200,
				 plot_width=400,
				 x_range=(1, 10),
				 tools=['xpan', 'reset', 'save'])

	fig.vbar(x='Game',
			 top=stat_col,
			 source=nugget_stats,
			 width=0.9,
			 color=dict(field='Win/Loss', transform=win_loss_mapper))

	hover_glyph = fig.vbar(x='Game',
			 top=stat_col,
			 source=nugget_stats,
			 width=0.9,
			 alpha=0,
			 hover_fill_color='lightgray',
			 hover_fill_alpha=0.25)

	fig.add_tools(HoverTool(tooltips=hover_info, renderers=[hover_glyph]))

	stat_figs[stat_label] = fig

# Layout
grid = gridplot([[stat_figs['Points'], stat_figs['Assists']],
				 [stat_figs['Rebounds'], stat_figs['Turnovers']]])

# Join X axes
stat_figs['Points'].x_range = \
	stat_figs['Assists'].x_range = \
	stat_figs['Rebounds'].x_range = \
	stat_figs['Turnovers'].x_range

html = """<h3>Denver Nuggets Game Statistics</h3>
<b><i>2017-18 Regular Season</i></b>
<br>
<i>Wins in green, losses in red</i>
"""
sup_title = Div(text=html)

show(column(sup_title, grid)) 





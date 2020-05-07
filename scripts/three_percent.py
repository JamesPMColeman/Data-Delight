from bokeh.io import output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.plotting import figure, show

from read_nba_data import three_takers


# Create output location
output_file('three_point_percent.html',
			title='Three_Point_Percent')

# Store the data in a CDS
three_shooters = ColumnDataSource(three_takers)

# Specify the selection tools
select_tools = ['box_select',
				'lasso_select',
				'poly_select']

# Create figure
fig = figure(plot_height=400,
			 plot_width=600,
			 x_axis_label='Three-Point Shots',
			 y_axis_label='Three-Point Percent',
			 title='3pt Percent',
			 toolbar_location='below',
			 tools=select_tools)

fig.yaxis[0].formatter = NumeralTickFormatter(format='00.0%')

fig.square(x='play3PA',
		   y='pct3PM',
		   source=three_shooters,
		   color='royalblue',
		   selection_color='deepskyblue',
		   nonselection_color='lightgray',
		   nonselection_alpha=0.3)

show(fig)
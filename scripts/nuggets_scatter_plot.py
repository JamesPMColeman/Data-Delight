from bokeh.io import output_file
from bokeh.models import ColumnDataSource,\
    CategoricalColorMapper, NumeralTickFormatter
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show

from read_nba_data import nuggets_2

output_file('nugget_scatter.html', title='Nuggets Statistics')

nugget_stats = ColumnDataSource(nuggets_2)

# Create categorical color mapper
win_loss_mapper = CategoricalColorMapper(
    factors=['W', 'L'],
    palette=['green', 'red'])

# Tools
tool_list = ['lasso_select', 'tap', 'reset', 'save']

# Figure of 2pt% vs 3pt%
pct_fig = figure(
    title='2Pt FG % vs 3Pt FG %',
    plot_height=400,
    plot_width=400,
    tools=tool_list,
    x_axis_label='2Pt FG',
    y_axis_label='3Pt FG'
    )

# Circle markers
pct_fig.circle(
    x='team2P%',
    y='team3P%',
    source=nugget_stats,
    size=12,
    color='black'
    )

# X and Y gradient
pct_fig.xaxis[0].formatter = NumeralTickFormatter(format='00.0%')
pct_fig.yaxis[0].formatter = NumeralTickFormatter(format='00.0%')

# Comparison figure
total_fig = figure(
    title='Team Points vs Opponent Points',
    plot_height=400,
    plot_width=400,
    tools=tool_list,
    x_axis_label='Team Points',
    y_axis_label='Opponent Points'
    )

# Square marks
total_fig.square(
    x='teamPTS',
    y='opptPTS',
    source=nugget_stats,
    size=10,
    color=dict(field='Win/Loss', transform=win_loss_mapper)
    )

# Layout
grid = gridplot([[pct_fig, total_fig]])

show(grid)

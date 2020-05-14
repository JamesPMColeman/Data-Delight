from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource


from read_nba_data import west_top_2


output_file(
    'west_top_2_standings_race.html',
    title='Western Conference Top 2 Teams Wins'
    )

# Isolate the Rockets and the Warriors
rockets = west_top_2[west_top_2['teamAbbr'] == 'HOU']
warriors = west_top_2[west_top_2['teamAbbr'] == 'GS']

# Create ColumnDataSources
rockets_column = ColumnDataSource(rockets)
warriors_column = ColumnDataSource(warriors)

# Create figure
fig = figure(
    x_axis_type='datetime',
    plot_height=300,
    plot_width=600,
    title='Western Conference Top 2 Teams Wins',
    toolbar_location=None
    )

# Render specs
fig.step(
    'stDate',
    'gameWon',
    color='#CE1141',
    legend_label='rockets',
    source=rockets_column
    )

fig.step(
    'stDate',
    'gameWon',
    color='#006BB6',
    legend_label='warriors',
    source=warriors_column
    )

fig.legend.location = 'top_left'

show(fig)
